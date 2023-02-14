import re
import html
import json
import requests
from typing import Union
from dataclasses import dataclass, field
from xml.etree.ElementTree import ElementTree

from .xml import XmlBuilder


@dataclass(repr=True)
class Version:
    """Bedrock Version class"""
    version: str
    update_id: str
    is_beta: bool
    is_deprecated: bool
    uri: str

    def __init__(
        self,
        version: str,
        update_id: str,
        is_beta: bool = False
    ):
        self.version = version
        self.update_id = update_id
        self.is_beta = bool(is_beta)
        self.uri = self._get_uri()
        self.is_deprecated = not self.uri and not self.is_beta

    def _get_uri(self) -> Union[str, None]:
        """Get version .appx file direct URI"""
        builder = XmlBuilder()
        tree = builder.build(self.update_id)
        return self._get_appx_uri_from_xml_tree(tree)

    def _get_appx_uri_from_xml_tree(self, tree_root: ElementTree) -> Union[str, None]:
        """Get update .appx direct download URI using builded SOAP XML tree
        to get update info
        
        :param tree_root: Tree root element
        :type tree_root: ElementTree

        :return: .appx file URI or None
        :rtype: Union[str, None]
        """
        xml_string = XmlBuilder.stringify(tree_root)
        content = self._query_update_content(xml_string)
        return self._parse_appx_uri(content)

    def _query_update_content(self, xml: str):
        """Query Microsoft Update info using generated XML soap schema
        
        :param xml: Stringified XML schema
        :type xml: str
        """
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0 Win64 x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36 OPR/79.0.4143.73',
            'Content-Type': 'application/soap+xml; charset=utf-8'
        }
        response = requests.post("https://fe3.delivery.mp.microsoft.com/ClientWebService/client.asmx/secured", data=xml, headers=headers, verify=False)
        return response.content.decode('utf-8')

    def _parse_appx_uri(self, source: str) -> Union[str, None]:
        """Parse .appx package URI from the response

        :param source: Source string to parse
        :type source: str

        :return: .appx file URI or None
        :rtype: Union[str, None]
        """
        url = re.search(r"<Url>(http://tlu\.dl\.delivery\.mp\.microsoft\.com.+?)<\/Url>", source)
        return html.unescape(url.group(1)) if url else None


class Versions:
    """Version class

    Provides functionality to interact with Minecraft Bedrock versions
    """
    url = "https://raw.githubusercontent.com/MCMrARM/mc-w10-versiondb/master/versions.json.min"

    @classmethod
    def get_all(cls):
        """Get all available versions"""
        response = requests.get(cls.url)
        for ver in json.loads(response.content):
            yield Version(*ver)

    @classmethod
    def get_count(cls):
        """Get all available versions count"""
        response = requests.get(cls.url)
        return len(json.loads(response.content))

    @classmethod
    def get_by_version(cls, version: str) -> Union[Version, None]:
        """Get version instance by its version
        
        :param version: Minecraft Bedrock Version (for ex. 1.8.0.24)
        :type version: str
        
        :return: Version class instance
        :rtype: Version
        """
        response = requests.get(cls.url)
        for ver in json.loads(response.content):
            if ver[0] == version:
                return Version(*ver)
