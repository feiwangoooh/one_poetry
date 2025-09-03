from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

import requests


class OnePoetryTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:

        try:
            response = requests.get("https://v1.jinrishici.com/all.json", timeout=5)
            response.raise_for_status()

            data = response.json()

            format_str = f"""\r\n{str(data["content"])}\r\n——{str(data["author"])}《{str(data["origin"])}》\r\n"""

            yield self.create_text_message(format_str)

        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to retrieve data: {str(e)}")
        except ValueError as e:
            raise Exception(f"Failed to parse data: {str(e)}")
