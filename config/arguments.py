# external imports
from argparse import ArgumentParser

import torch
from pydantic import BaseModel, Field

# internal imports


class Arguments(BaseModel):
    """Arguments class for the main script."""

    # name
    name: str = Field(default="pytorch-template", title="n", description="name")

    # training
    device: str = Field(
        default="cuda" if torch.cuda.is_available() else "cpu",
        title="d",
        description="device",
    )

    @classmethod
    def parse_args(cls: "Arguments"):  # noqa: ANN206
        """Parse arguments."""
        parser = ArgumentParser()
        properties: dict = cls.model_json_schema()["properties"]
        for v in properties.values():
            arg = {}
            arg["name_or_flags"] = [f"-{v['title']}", f"--{v['description']}"]
            if v["default"]:
                arg["default"] = v["default"]
            else:
                arg["required"] = True
            if v["description"]:
                arg["help"] = v["description"]
            if v["type"]:
                arg["type"] = cls._convert_json_schema_type_to_argparse_type(v["type"])
            parser.add_argument(
                *arg["name_or_flags"],
                default=arg.get("default"),
                help=arg.get("help"),
                type=arg.get("type"),
                required=arg.get("required"),
            )
        return cls.model_validate(parser.parse_args().__dict__)

    @staticmethod
    def _convert_json_schema_type_to_argparse_type(json_schema_type: str) -> type:
        """Convert JSON schema type to argparse type."""
        if json_schema_type == "string":
            return str
        if json_schema_type == "integer":
            return int
        if json_schema_type == "number":
            return float
        if json_schema_type == "boolean":
            return bool
        if json_schema_type == "array":
            return list
        value_error = f"Invalid JSON schema type: {json_schema_type}"
        raise ValueError(value_error)
