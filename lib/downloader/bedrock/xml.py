import urllib3
from datetime import datetime, timedelta
import xml.etree.cElementTree as ET


DEFAULT_URL = "https://fe3.delivery.mp.microsoft.com/ClientWebService/client.asmx"
SECURED_URL = "https://fe3.delivery.mp.microsoft.com/ClientWebService/client.asmx/secured"
SUAP_URI = "http://www.w3.org/2003/05/soap-envelope"
ADDRESSING_URI = "http://www.w3.org/2005/08/addressing"
SECEXT_URI = "http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd"
SECUTIL_URI = "http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd"
AUTHORIZATION_URI = "http://schemas.microsoft.com/msus/2014/10/WindowsUpdateAuthorization"
CLIENT_WEB_SERVICE_URI = "http://www.microsoft.com/SoftwareDistribution/Server/ClientWebService"
ACTION_METHOD_URI = "GetExtendedUpdateInfo2"
DEVICE_ATTRS = "E:BranchReadinessLevel=CBB&DchuNvidiaGrfxExists=1&ProcessorIdentifier=Intel64%20Family%206%20Model\
%2063%20Stepping%202&CurrentBranch=rs4_release&DataVer_RS5=1942&FlightRing=Retail&AttrDataVer=57&\
InstallLanguage=en-US&DchuAmdGrfxExists=1&OSUILocale=en-US&InstallationType=Client&FlightingBranchName=&\
Version_RS5=10&UpgEx_RS5=Green&GStatus_RS5=2&OSSkuId=48&App=WU&InstallDate=1529700913&ProcessorManufacturer=GenuineIntel&\
AppVer=10.0.17134.471&OSArchitecture=AMD64&UpdateManagementGroup=2&IsDeviceRetailDemo=0&\
HidOverGattReg=C%3A%5CWINDOWS%5CSystem32%5CDriverStore%5CFileRepository%5Chidbthle.inf_amd64_467f181075371c89%5CMicrosoft.\
Bluetooth.Profiles.HidOverGatt.dll&IsFlightingEnabled=0&DchuIntelGrfxExists=1&TelemetryLevel=1&\
DefaultUserRegion=244&DeferFeatureUpdatePeriodInDays=365&Bios=Unknown&WuClientVer=10.0.17134.471&\
PausedFeatureStatus=1&Steam=URL%3Asteam%20protocol&Free=8to16&OSVersion=10.0.17134.472&DeviceFamily=Windows.Desktop"

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class XmlBuilder:
    def __init__(self):
        pass

    @classmethod
    def _get_datetime(self):
        """Get current datetime and expiration datetime"""
        now = datetime.now()
        return now, now + timedelta(minutes=5)

    def build(self, update_id: str) -> ET.ElementTree:
        """Build an XML tree for the given Microsoft update Id
        
        :param update_id: Microsoft Update Id
        :type update_id: str
        
        :return: XML tree for perfoming request
        :rtype: ET.ElementTree
        """
        now, exp = map(datetime.isoformat, self._get_datetime())

        root = ET.Element(f"s:Envelope", {
            "xmlns:s": SUAP_URI,
            "xmlns:a": ADDRESSING_URI
        })
        # Header
        header = ET.SubElement(root, "s:Header")
        ET.SubElement(header, "a:Action", {"s:mustUnderstand": "1"}).text = f"{CLIENT_WEB_SERVICE_URI}/{ACTION_METHOD_URI}"
        ET.SubElement(header, "a:MessageID").text = "urn:uuid:5754a03d-d8d5-489f-b24d-efc31b3fd32d"
        ET.SubElement(header, "a:To", {"s:mustUnderstand": "1"}).text = SECURED_URL

        # Security
        sec = ET.SubElement(header, "o:Security", {"s:mustUnderstand": "1", "xmlns:o": SECEXT_URI})
        # Tiestamp
        ts = ET.SubElement(sec, "Timestamp", {"xmlns": SECUTIL_URI})
        ET.SubElement(ts, "Created").text = now
        ET.SubElement(ts, "Expires").text = exp
        # WindowsUpdateTicketsToken
        wutt = ET.SubElement(sec, "wuws:WindowsUpdateTicketsToken", {
            "wsu:id": "ClientMSA",
            "xmlns:wsu": SECUTIL_URI,
            "xmlns:wuws": AUTHORIZATION_URI
        })
        ET.SubElement(wutt, "TicketType", {
            "Name": "AAD",
            "Version": "1.0",
            "Policy": "MBI_SSL"
        })

        # Body
        body = ET.SubElement(root, "s:Body")
        geui = ET.SubElement(body, "GetExtendedUpdateInfo2", xmlns=CLIENT_WEB_SERVICE_URI)
        uids = ET.SubElement(geui, "updateIDs")
        uident = ET.SubElement(uids, "UpdateIdentity")
        ET.SubElement(uident, "UpdateID").text = update_id
        ET.SubElement(uident, "RevisionNumber").text = "1"
        itypes = ET.SubElement(geui, "infoTypes")
        ET.SubElement(itypes, "XmlUpdateFragmentType").text = "FileUrl"
        ET.SubElement(geui, "deviceAttributes").text = DEVICE_ATTRS

        return ET.ElementTree(root)

    @classmethod
    def stringify(cls, tree: ET.ElementTree):
        """Convert an XML tree to string
        """
        root = tree.getroot()
        return ET.tostring(root)
