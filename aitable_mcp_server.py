# Minimal MCP server for AITable.ai API integration in Windsurf
# Requires: pip install modelcontextprotocol requests
import os
import requests
from modelcontextprotocol.server import FastMCP, Tool

class AITableMCPServer(FastMCP):
    @Tool
    def get_table_records(self, datasheet_id: str):
        """Fetch records from an AITable.ai datasheet (table)."""
        api_key = os.getenv("AITABLE_API_KEY", "")
        base_url = "https://api.aitable.ai"
        url = f"{base_url}/fusion/v1/datasheets/{datasheet_id}/records"
        headers = {"Authorization": f"Bearer {api_key}"}
        resp = requests.get(url, headers=headers)
        return resp.json()

    @Tool
    def add_record(self, datasheet_id: str, fields: dict):
        """Add a record to an AITable.ai datasheet."""
        api_key = os.getenv("AITABLE_API_KEY", "")
        base_url = "https://api.aitable.ai"
        url = f"{base_url}/fusion/v1/datasheets/{datasheet_id}/records"
        headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
        payload = {"records": [{"fields": fields}]}
        resp = requests.post(url, headers=headers, json=payload)
        return resp.json()

    @Tool
    def update_record(self, datasheet_id: str, record_id: str, fields: dict):
        """Update a record in an AITable.ai datasheet."""
        api_key = os.getenv("AITABLE_API_KEY", "")
        base_url = "https://api.aitable.ai"
        url = f"{base_url}/fusion/v1/datasheets/{datasheet_id}/records/{record_id}"
        headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
        payload = {"fields": fields}
        resp = requests.patch(url, headers=headers, json=payload)
        return resp.json()

    @Tool
    def delete_record(self, datasheet_id: str, record_id: str):
        """Delete a record from an AITable.ai datasheet."""
        api_key = os.getenv("AITABLE_API_KEY", "")
        base_url = "https://api.aitable.ai"
        url = f"{base_url}/fusion/v1/datasheets/{datasheet_id}/records/{record_id}"
        headers = {"Authorization": f"Bearer {api_key}"}
        resp = requests.delete(url, headers=headers)
        return resp.json() if resp.content else {'status': resp.status_code}

    @Tool
    def upload_attachment(self, datasheet_id: str, file_path: str):
        """Upload a file as an attachment to an AITable.ai datasheet."""
        api_key = os.getenv("AITABLE_API_KEY", "")
        base_url = "https://api.aitable.ai"
        url = f"{base_url}/fusion/v1/datasheets/{datasheet_id}/attachments/upload"
        headers = {"Authorization": f"Bearer {api_key}"}
        with open(file_path, 'rb') as f:
            files = {'file': f}
            resp = requests.post(url, headers=headers, files=files)
        return resp.json()

if __name__ == "__main__":
    AITableMCPServer().run()
