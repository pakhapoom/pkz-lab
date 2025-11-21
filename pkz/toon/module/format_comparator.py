import csv
import io
import json
from typing import Any

import yaml
from toon_format import encode as toon_encode

from pkz.toon.module.token_counter import TokenCounter


class FormatComparator:
    """Compare token counts across different serialization formats."""

    def __init__(self, encoding_name: str = "o200k_base"):
        """
        Initialize a FormatComparison with a specific encoding.

        Args:
            encoding_name: The tiktoken encoding to use (default: "o200k_base" for GPT-4o)
        """
        self.counter = TokenCounter(encoding_name)

    def _to_json(self, data: Any, compact: bool = False) -> str:
        """Convert data to JSON format."""
        if compact:
            return json.dumps(data, separators=(",", ":"))
        return json.dumps(data, indent=2)

    def _to_yaml(self, data: Any) -> str:
        """Convert data to YAML format."""
        return yaml.dump(data, default_flow_style=False, sort_keys=False)

    def _to_toon(self, data: Any) -> str:
        """Convert data to TOON format."""
        return toon_encode(data)

    def _to_csv(self, data: Any) -> str:
        """
        Convert data to CSV format.
        Only works for list of dictionaries with uniform keys.
        """
        if not isinstance(data, list) or not data:
            raise ValueError("CSV format requires a non-empty list of dictionaries")

        if not all(isinstance(item, dict) for item in data):
            raise ValueError("CSV format requires all items to be dictionaries")

        output = io.StringIO()
        keys = data[0].keys()
        writer = csv.DictWriter(output, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)
        return output.getvalue()

    def _to_xml(self, data: Any, root_tag: str = "root") -> str:
        """
        Convert data to simple XML format.
        Note: This is a basic implementation and may not handle all data structures.
        """

        def _dict_to_xml(d: dict, parent_tag: str = "item") -> str:
            xml_parts = [f"<{parent_tag}>"]
            for key, value in d.items():
                if isinstance(value, dict):
                    xml_parts.append(_dict_to_xml(value, key))
                elif isinstance(value, list):
                    for item in value:
                        if isinstance(item, dict):
                            xml_parts.append(_dict_to_xml(item, key))
                        else:
                            xml_parts.append(f"<{key}>{item}</{key}>")
                else:
                    xml_parts.append(f"<{key}>{value}</{key}>")
            xml_parts.append(f"</{parent_tag}>")
            return "".join(xml_parts)

        if isinstance(data, list):
            xml_parts = [f"<{root_tag}>"]
            for item in data:
                if isinstance(item, dict):
                    xml_parts.append(_dict_to_xml(item, "item"))
                else:
                    xml_parts.append(f"<item>{item}</item>")
            xml_parts.append(f"</{root_tag}>")
            return "".join(xml_parts)
        elif isinstance(data, dict):
            return _dict_to_xml(data, root_tag)
        else:
            return f"<{root_tag}>{data}</{root_tag}>"

    def compare(self, data: Any, include_csv: bool = True, include_xml: bool = True) -> dict:
        """
        Compare token counts across different formats.

        Args:
            data: The data to compare across formats
            include_csv: Whether to include CSV format (only works for list of dicts)
            include_xml: Whether to include XML format

        Returns:
            Dictionary with format names as keys and token counts as values
        """
        results = {}

        # JSON (baseline)
        json_text = self._to_json(data, compact=False)
        results["JSON"] = self.counter.count(json_text)

        # JSON compact
        json_compact_text = self._to_json(data, compact=True)
        results["JSON compact"] = self.counter.count(json_compact_text)

        # YAML
        yaml_text = self._to_yaml(data)
        results["YAML"] = self.counter.count(yaml_text)

        # TOON
        toon_text = self._to_toon(data)
        results["TOON"] = self.counter.count(toon_text)

        # CSV (optional, only for tabular data)
        if include_csv:
            try:
                csv_text = self._to_csv(data)
                results["CSV"] = self.counter.count(csv_text)
            except ValueError:
                pass  # Skip CSV if data is not suitable

        # XML (optional)
        if include_xml:
            try:
                xml_text = self._to_xml(data)
                results["XML"] = self.counter.count(xml_text)
            except Exception:
                pass  # Skip XML if conversion fails

        return results

    def calculate_percentage_change(self, results: dict) -> dict:
        """
        Calculate percentage change from JSON compact baseline.

        Args:
            results: Dictionary with format names and token counts

        Returns:
            Dictionary with format names and percentage change from JSON compact
        """
        baseline = results.get("JSON compact", 0)
        if baseline == 0:
            raise ValueError("JSON compact baseline cannot be zero")

        percentage_changes = {}
        for format_name, token_count in results.items():
            change = ((token_count - baseline) / baseline) * 100
            percentage_changes[format_name] = change

        return percentage_changes

    def display_format(self, data: Any, format_name: str) -> str:
        """
        Display data in a specific format.

        Args:
            data: The data to display
            format_name: The format to use ('json', 'json_compact', 'yaml', 'toon', 'csv', 'xml')

        Returns:
            The formatted string representation

        Raises:
            ValueError: If format_name is not supported
        """
        format_name_lower = format_name.lower()

        if format_name_lower == "json":
            return self._to_json(data, compact=False)
        elif format_name_lower == "json_compact":
            return self._to_json(data, compact=True)
        elif format_name_lower == "yaml":
            return self._to_yaml(data)
        elif format_name_lower == "toon":
            return self._to_toon(data)
        elif format_name_lower == "csv":
            return self._to_csv(data)
        elif format_name_lower == "xml":
            return self._to_xml(data)
        else:
            raise ValueError(
                f"Unsupported format: {format_name}. "
                f"Supported formats: json, json_compact, yaml, toon, csv, xml"
            )

    def display_toon(self, data: Any) -> str:
        """
        Display data in TOON format.

        Args:
            data: The data to display

        Returns:
            The TOON formatted string
        """
        return self._to_toon(data)

    def display_json_compact(self, data: Any) -> str:
        """
        Display data in compact JSON format (no whitespace).

        Args:
            data: The data to display

        Returns:
            The compact JSON formatted string
        """
        return self._to_json(data, compact=True)

    def display_json(self, data: Any) -> str:
        """
        Display data in pretty-printed JSON format.

        Args:
            data: The data to display

        Returns:
            The pretty-printed JSON formatted string
        """
        return self._to_json(data, compact=False)

    def display_yaml(self, data: Any) -> str:
        """
        Display data in YAML format.

        Args:
            data: The data to display

        Returns:
            The YAML formatted string
        """
        return self._to_yaml(data)

    def display_csv(self, data: Any) -> str:
        """
        Display data in CSV format.
        Only works for list of dictionaries with uniform keys.

        Args:
            data: The data to display (must be a list of dicts)

        Returns:
            The CSV formatted string

        Raises:
            ValueError: If data is not suitable for CSV format
        """
        return self._to_csv(data)

    def display_xml(self, data: Any, root_tag: str = "root") -> str:
        """
        Display data in XML format.

        Args:
            data: The data to display
            root_tag: The root XML tag name

        Returns:
            The XML formatted string
        """
        return self._to_xml(data, root_tag=root_tag)

    def print_comparison(
        self,
        data: Any,
        include_csv: bool = True,
        include_xml: bool = True,
    ):
        """
        Print a formatted comparison of token counts.

        Args:
            data: The data to compare across formats
            include_csv: Whether to include CSV format
            include_xml: Whether to include XML format
        """
        results = self.compare(data, include_csv=include_csv, include_xml=include_xml)
        percentage_changes = self.calculate_percentage_change(results)

        # Sort by percentage change (descending)
        sorted_formats = sorted(percentage_changes.items(), key=lambda x: x[1], reverse=True)

        print("Token Count Comparison")
        print("=" * 60)
        print(f"{'Format':<20} {'Tokens':<10} {'Change from JSON compact':<20}")
        print("-" * 60)

        for format_name, change in sorted_formats:
            token_count = results[format_name]
            sign = "+" if change > 0 else ""
            print(f"{format_name:<20} {token_count:<10} {sign}{change:.2f}%")

        print("=" * 60)
