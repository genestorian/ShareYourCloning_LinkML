from __future__ import annotations
from datetime import datetime, date, time
from decimal import Decimal
from enum import Enum
import re
import sys
from typing import Any, ClassVar, List, Literal, Dict, Optional, Union
from pydantic import BaseModel, ConfigDict, Field, RootModel, field_validator

metamodel_version = "None"
version = "None"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        validate_assignment=True,
        validate_default=True,
        extra="forbid",
        arbitrary_types_allowed=True,
        use_enum_values=True,
        strict=False,
    )
    pass


class LinkMLMeta(RootModel):
    root: Dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key: str):
        return getattr(self.root, key)

    def __getitem__(self, key: str):
        return self.root[key]

    def __setitem__(self, key: str, value):
        self.root[key] = value

    def __contains__(self, key: str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta(
    {
        "default_prefix": "shareyourcloning_linkml",
        "default_range": "string",
        "description": "A LinkML data model for ShareYourCloning",
        "id": "https://w3id.org/genestorian/ShareYourCloning_LinkML",
        "imports": ["linkml:types"],
        "license": "MIT",
        "name": "ShareYourCloning_LinkML",
        "prefixes": {
            "OBI": {"prefix_prefix": "OBI", "prefix_reference": "http://purl.obolibrary.org/obo/OBI_"},
            "PATO": {"prefix_prefix": "PATO", "prefix_reference": "http://purl.obolibrary.org/obo/PATO_"},
            "biolink": {"prefix_prefix": "biolink", "prefix_reference": "https://w3id.org/biolink/"},
            "example": {"prefix_prefix": "example", "prefix_reference": "https://example.org/"},
            "linkml": {"prefix_prefix": "linkml", "prefix_reference": "https://w3id.org/linkml/"},
            "schema": {"prefix_prefix": "schema", "prefix_reference": "http://schema.org/"},
            "shareyourcloning_linkml": {
                "prefix_prefix": "shareyourcloning_linkml",
                "prefix_reference": "https://w3id.org/genestorian/ShareYourCloning_LinkML/",
            },
        },
        "see_also": ["https://genestorian.github.io/ShareYourCloning_LinkML"],
        "source_file": "src/shareyourcloning_linkml/schema/shareyourcloning_linkml.yaml",
        "title": "ShareYourCloning_LinkML",
    }
)


class RepositoryName(str, Enum):
    # Addgene
    addgene = "addgene"
    # GenBank
    genbank = "genbank"
    # Benchling
    benchling = "benchling"


class SequenceFileFormat(str, Enum):
    fasta = "fasta"
    genbank = "genbank"
    snapgene = "snapgene"
    embl = "embl"


class AddGeneSequenceType(str, Enum):
    # Full sequence of the plasmid submitted by the depositor
    depositor_full = "depositor-full"
    # Full sequence of the plasmid performed by Addgene
    addgene_full = "addgene-full"


class NamedThing(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {"class_uri": "schema:Thing", "from_schema": "https://w3id.org/genestorian/ShareYourCloning_LinkML"}
    )

    id: int = Field(
        ...,
        description="""A unique identifier for a thing""",
        json_schema_extra={
            "linkml_meta": {"alias": "id", "domain_of": ["NamedThing", "Sequence"], "slot_uri": "schema:identifier"}
        },
    )


class Sequence(NamedThing):
    """
    Represents a sequence
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {"abstract": True, "from_schema": "https://w3id.org/genestorian/ShareYourCloning_LinkML"}
    )

    id: int = Field(
        ...,
        description="""A unique identifier for a thing""",
        json_schema_extra={
            "linkml_meta": {"alias": "id", "domain_of": ["NamedThing", "Sequence"], "slot_uri": "schema:identifier"}
        },
    )
    type: Literal["Sequence"] = Field(
        "Sequence",
        description="""The type of the source""",
        json_schema_extra={
            "linkml_meta": {"alias": "type", "designates_type": True, "domain_of": ["Sequence", "Source"]}
        },
    )


class TextFileSequence(Sequence):
    """
    A sequence (may have features) defined by the content of a text file
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "from_schema": "https://w3id.org/genestorian/ShareYourCloning_LinkML",
            "slot_usage": {
                "overhang_crick_3prime": {"ifabsent": "int(0)", "name": "overhang_crick_3prime"},
                "overhang_watson_3prime": {"ifabsent": "int(0)", "name": "overhang_watson_3prime"},
                "sequence_file_format": {"name": "sequence_file_format", "required": True},
            },
        }
    )

    sequence_file_format: SequenceFileFormat = Field(
        ...,
        description="""The format of a sequence file""",
        json_schema_extra={
            "linkml_meta": {"alias": "sequence_file_format", "domain_of": ["TextFileSequence", "UploadedFileSource"]}
        },
    )
    overhang_crick_3prime: Optional[int] = Field(
        0,
        description="""Taken from pydna's `dseq::ovhg`An integer describing the length of the crick strand overhang in the 5' of the molecule, or 3' of the crick strand""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "overhang_crick_3prime",
                "domain_of": ["TextFileSequence", "ManuallyTypedSource", "OligoHybridizationSource"],
                "ifabsent": "int(0)",
            }
        },
    )
    overhang_watson_3prime: Optional[int] = Field(
        0,
        description="""The equivalent of `overhang_crick_3prime` but for the watson strand""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "overhang_watson_3prime",
                "domain_of": ["TextFileSequence", "ManuallyTypedSource"],
                "ifabsent": "int(0)",
            }
        },
    )
    file_content: Optional[str] = Field(
        None, json_schema_extra={"linkml_meta": {"alias": "file_content", "domain_of": ["TextFileSequence"]}}
    )
    id: int = Field(
        ...,
        description="""A unique identifier for a thing""",
        json_schema_extra={
            "linkml_meta": {"alias": "id", "domain_of": ["NamedThing", "Sequence"], "slot_uri": "schema:identifier"}
        },
    )
    type: Literal["TextFileSequence"] = Field(
        "TextFileSequence",
        description="""The type of the source""",
        json_schema_extra={
            "linkml_meta": {"alias": "type", "designates_type": True, "domain_of": ["Sequence", "Source"]}
        },
    )


class Primer(Sequence):
    """
    An oligonucleotide or primer
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {"from_schema": "https://w3id.org/genestorian/ShareYourCloning_LinkML"}
    )

    name: Optional[str] = Field(
        None,
        description="""A human-readable name for a thing""",
        json_schema_extra={"linkml_meta": {"alias": "name", "domain_of": ["Primer"], "slot_uri": "schema:name"}},
    )
    sequence: Optional[str] = Field(
        None, json_schema_extra={"linkml_meta": {"alias": "sequence", "domain_of": ["Primer", "AssemblyFragment"]}}
    )
    id: int = Field(
        ...,
        description="""A unique identifier for a thing""",
        json_schema_extra={
            "linkml_meta": {"alias": "id", "domain_of": ["NamedThing", "Sequence"], "slot_uri": "schema:identifier"}
        },
    )
    type: Literal["Primer"] = Field(
        "Primer",
        description="""The type of the source""",
        json_schema_extra={
            "linkml_meta": {"alias": "type", "designates_type": True, "domain_of": ["Sequence", "Source"]}
        },
    )

    @field_validator("sequence")
    def pattern_sequence(cls, v):
        pattern = re.compile(r"^[acgtACGT]+$")
        if isinstance(v, list):
            for element in v:
                if not pattern.match(element):
                    raise ValueError(f"Invalid sequence format: {element}")
        elif isinstance(v, str):
            if not pattern.match(v):
                raise ValueError(f"Invalid sequence format: {v}")
        return v


class SequenceCut(ConfiguredBaseModel):
    """
    Represents a cut in a DNA sequence
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {"from_schema": "https://w3id.org/genestorian/ShareYourCloning_LinkML"}
    )

    cut_watson: int = Field(
        ...,
        description="""The position of the cut in the watson strand. The cut is made before the base at this position (zero-based), so that cut position 1 cuts after the first base.""",
        json_schema_extra={"linkml_meta": {"alias": "cut_watson", "domain_of": ["SequenceCut"]}},
    )
    overhang: int = Field(
        ...,
        description="""The length of the overhang that is left after the cut. It can be negative, same meaning as in pydna's `dseq::ovhg` and biopython's `Bio.Restriction.RestrictionType.ovhg`.""",
        json_schema_extra={"linkml_meta": {"alias": "overhang", "domain_of": ["SequenceCut"]}},
    )


class RestrictionSequenceCut(SequenceCut):
    """
    Represents a cut in a DNA sequence that is made by a restriction enzyme
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "from_schema": "https://w3id.org/genestorian/ShareYourCloning_LinkML",
            "slot_usage": {"restriction_enzyme": {"name": "restriction_enzyme", "required": True}},
        }
    )

    restriction_enzyme: str = Field(
        ...,
        json_schema_extra={
            "linkml_meta": {
                "alias": "restriction_enzyme",
                "domain_of": ["RestrictionSequenceCut"],
                "exact_mappings": ["OBI:0000732"],
            }
        },
    )
    cut_watson: int = Field(
        ...,
        description="""The position of the cut in the watson strand. The cut is made before the base at this position (zero-based), so that cut position 1 cuts after the first base.""",
        json_schema_extra={"linkml_meta": {"alias": "cut_watson", "domain_of": ["SequenceCut"]}},
    )
    overhang: int = Field(
        ...,
        description="""The length of the overhang that is left after the cut. It can be negative, same meaning as in pydna's `dseq::ovhg` and biopython's `Bio.Restriction.RestrictionType.ovhg`.""",
        json_schema_extra={"linkml_meta": {"alias": "overhang", "domain_of": ["SequenceCut"]}},
    )


class Source(NamedThing):
    """
    Represents the source of a sequence
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {"abstract": True, "from_schema": "https://w3id.org/genestorian/ShareYourCloning_LinkML"}
    )

    input: Optional[List[int]] = Field(
        None,
        description="""The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.""",
        json_schema_extra={"linkml_meta": {"alias": "input", "domain_of": ["Source"]}},
    )
    output: Optional[int] = Field(
        None,
        description="""Identifier of the sequence that is the output of this source.""",
        json_schema_extra={"linkml_meta": {"alias": "output", "domain_of": ["Source"]}},
    )
    type: Literal["Source"] = Field(
        "Source",
        description="""The type of the source""",
        json_schema_extra={
            "linkml_meta": {"alias": "type", "designates_type": True, "domain_of": ["Sequence", "Source"]}
        },
    )
    output_name: Optional[str] = Field(
        None,
        description="""Used to specify the name of the output sequence""",
        json_schema_extra={"linkml_meta": {"alias": "output_name", "domain_of": ["Source"]}},
    )
    id: int = Field(
        ...,
        description="""A unique identifier for a thing""",
        json_schema_extra={
            "linkml_meta": {"alias": "id", "domain_of": ["NamedThing", "Sequence"], "slot_uri": "schema:identifier"}
        },
    )


class ManuallyTypedSource(Source):
    """
    Represents the source of a sequence that is manually typed by the user
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "from_schema": "https://w3id.org/genestorian/ShareYourCloning_LinkML",
            "slot_usage": {
                "overhang_crick_3prime": {"ifabsent": "int(0)", "name": "overhang_crick_3prime"},
                "overhang_watson_3prime": {"ifabsent": "int(0)", "name": "overhang_watson_3prime"},
            },
        }
    )

    overhang_crick_3prime: Optional[int] = Field(
        0,
        description="""Taken from pydna's `dseq::ovhg`An integer describing the length of the crick strand overhang in the 5' of the molecule, or 3' of the crick strand""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "overhang_crick_3prime",
                "domain_of": ["TextFileSequence", "ManuallyTypedSource", "OligoHybridizationSource"],
                "ifabsent": "int(0)",
            }
        },
    )
    overhang_watson_3prime: Optional[int] = Field(
        0,
        description="""The equivalent of `overhang_crick_3prime` but for the watson strand""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "overhang_watson_3prime",
                "domain_of": ["TextFileSequence", "ManuallyTypedSource"],
                "ifabsent": "int(0)",
            }
        },
    )
    user_input: str = Field(
        ..., json_schema_extra={"linkml_meta": {"alias": "user_input", "domain_of": ["ManuallyTypedSource"]}}
    )
    circular: Optional[bool] = Field(
        None,
        description="""Whether the sequence is circular or not""",
        json_schema_extra={
            "linkml_meta": {"alias": "circular", "domain_of": ["ManuallyTypedSource", "AssemblySource"]}
        },
    )
    input: Optional[List[int]] = Field(
        None,
        description="""The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.""",
        json_schema_extra={"linkml_meta": {"alias": "input", "domain_of": ["Source"]}},
    )
    output: Optional[int] = Field(
        None,
        description="""Identifier of the sequence that is the output of this source.""",
        json_schema_extra={"linkml_meta": {"alias": "output", "domain_of": ["Source"]}},
    )
    type: Literal["ManuallyTypedSource"] = Field(
        "ManuallyTypedSource",
        description="""The type of the source""",
        json_schema_extra={
            "linkml_meta": {"alias": "type", "designates_type": True, "domain_of": ["Sequence", "Source"]}
        },
    )
    output_name: Optional[str] = Field(
        None,
        description="""Used to specify the name of the output sequence""",
        json_schema_extra={"linkml_meta": {"alias": "output_name", "domain_of": ["Source"]}},
    )
    id: int = Field(
        ...,
        description="""A unique identifier for a thing""",
        json_schema_extra={
            "linkml_meta": {"alias": "id", "domain_of": ["NamedThing", "Sequence"], "slot_uri": "schema:identifier"}
        },
    )

    @field_validator("user_input")
    def pattern_user_input(cls, v):
        pattern = re.compile(r"^[acgtACGT]+$")
        if isinstance(v, list):
            for element in v:
                if not pattern.match(element):
                    raise ValueError(f"Invalid user_input format: {element}")
        elif isinstance(v, str):
            if not pattern.match(v):
                raise ValueError(f"Invalid user_input format: {v}")
        return v


class UploadedFileSource(Source):
    """
    Represents the source of a sequence that is uploaded as a file
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "from_schema": "https://w3id.org/genestorian/ShareYourCloning_LinkML",
            "slot_usage": {"sequence_file_format": {"name": "sequence_file_format", "required": True}},
        }
    )

    sequence_file_format: SequenceFileFormat = Field(
        ...,
        description="""The format of a sequence file""",
        json_schema_extra={
            "linkml_meta": {"alias": "sequence_file_format", "domain_of": ["TextFileSequence", "UploadedFileSource"]}
        },
    )
    file_name: Optional[str] = Field(
        None,
        description="""The name of the file""",
        json_schema_extra={"linkml_meta": {"alias": "file_name", "domain_of": ["UploadedFileSource"]}},
    )
    index_in_file: Optional[int] = Field(
        None,
        description="""The index of the sequence in the file""",
        json_schema_extra={"linkml_meta": {"alias": "index_in_file", "domain_of": ["UploadedFileSource"]}},
    )
    circularize: Optional[bool] = Field(
        None,
        description="""Whether the sequence should be circularized (FASTA only)""",
        json_schema_extra={"linkml_meta": {"alias": "circularize", "domain_of": ["UploadedFileSource"]}},
    )
    input: Optional[List[int]] = Field(
        None,
        description="""The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.""",
        json_schema_extra={"linkml_meta": {"alias": "input", "domain_of": ["Source"]}},
    )
    output: Optional[int] = Field(
        None,
        description="""Identifier of the sequence that is the output of this source.""",
        json_schema_extra={"linkml_meta": {"alias": "output", "domain_of": ["Source"]}},
    )
    type: Literal["UploadedFileSource"] = Field(
        "UploadedFileSource",
        description="""The type of the source""",
        json_schema_extra={
            "linkml_meta": {"alias": "type", "designates_type": True, "domain_of": ["Sequence", "Source"]}
        },
    )
    output_name: Optional[str] = Field(
        None,
        description="""Used to specify the name of the output sequence""",
        json_schema_extra={"linkml_meta": {"alias": "output_name", "domain_of": ["Source"]}},
    )
    id: int = Field(
        ...,
        description="""A unique identifier for a thing""",
        json_schema_extra={
            "linkml_meta": {"alias": "id", "domain_of": ["NamedThing", "Sequence"], "slot_uri": "schema:identifier"}
        },
    )


class RepositoryIdSource(Source):
    """
    Represents the source of a sequence that is identified by a repository id
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {"from_schema": "https://w3id.org/genestorian/ShareYourCloning_LinkML"}
    )

    repository_id: str = Field(
        ...,
        description="""The id of the sequence in the repository""",
        json_schema_extra={"linkml_meta": {"alias": "repository_id", "domain_of": ["RepositoryIdSource"]}},
    )
    repository_name: RepositoryName = Field(
        ..., json_schema_extra={"linkml_meta": {"alias": "repository_name", "domain_of": ["RepositoryIdSource"]}}
    )
    input: Optional[List[int]] = Field(
        None,
        description="""The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.""",
        json_schema_extra={"linkml_meta": {"alias": "input", "domain_of": ["Source"]}},
    )
    output: Optional[int] = Field(
        None,
        description="""Identifier of the sequence that is the output of this source.""",
        json_schema_extra={"linkml_meta": {"alias": "output", "domain_of": ["Source"]}},
    )
    type: Literal["RepositoryIdSource"] = Field(
        "RepositoryIdSource",
        description="""The type of the source""",
        json_schema_extra={
            "linkml_meta": {"alias": "type", "designates_type": True, "domain_of": ["Sequence", "Source"]}
        },
    )
    output_name: Optional[str] = Field(
        None,
        description="""Used to specify the name of the output sequence""",
        json_schema_extra={"linkml_meta": {"alias": "output_name", "domain_of": ["Source"]}},
    )
    id: int = Field(
        ...,
        description="""A unique identifier for a thing""",
        json_schema_extra={
            "linkml_meta": {"alias": "id", "domain_of": ["NamedThing", "Sequence"], "slot_uri": "schema:identifier"}
        },
    )


class AddGeneIdSource(RepositoryIdSource):
    """
    Represents the source of a sequence that is identified by an AddGene id
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {"from_schema": "https://w3id.org/genestorian/ShareYourCloning_LinkML"}
    )

    sequence_file_url: Optional[str] = Field(
        None,
        description="""The URL of a sequence file""",
        json_schema_extra={"linkml_meta": {"alias": "sequence_file_url", "domain_of": ["AddGeneIdSource"]}},
    )
    addgene_sequence_type: Optional[AddGeneSequenceType] = Field(
        None, json_schema_extra={"linkml_meta": {"alias": "addgene_sequence_type", "domain_of": ["AddGeneIdSource"]}}
    )
    repository_id: str = Field(
        ...,
        description="""The id of the sequence in the repository""",
        json_schema_extra={"linkml_meta": {"alias": "repository_id", "domain_of": ["RepositoryIdSource"]}},
    )
    repository_name: RepositoryName = Field(
        ..., json_schema_extra={"linkml_meta": {"alias": "repository_name", "domain_of": ["RepositoryIdSource"]}}
    )
    input: Optional[List[int]] = Field(
        None,
        description="""The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.""",
        json_schema_extra={"linkml_meta": {"alias": "input", "domain_of": ["Source"]}},
    )
    output: Optional[int] = Field(
        None,
        description="""Identifier of the sequence that is the output of this source.""",
        json_schema_extra={"linkml_meta": {"alias": "output", "domain_of": ["Source"]}},
    )
    type: Literal["AddGeneIdSource"] = Field(
        "AddGeneIdSource",
        description="""The type of the source""",
        json_schema_extra={
            "linkml_meta": {"alias": "type", "designates_type": True, "domain_of": ["Sequence", "Source"]}
        },
    )
    output_name: Optional[str] = Field(
        None,
        description="""Used to specify the name of the output sequence""",
        json_schema_extra={"linkml_meta": {"alias": "output_name", "domain_of": ["Source"]}},
    )
    id: int = Field(
        ...,
        description="""A unique identifier for a thing""",
        json_schema_extra={
            "linkml_meta": {"alias": "id", "domain_of": ["NamedThing", "Sequence"], "slot_uri": "schema:identifier"}
        },
    )

    @field_validator("sequence_file_url")
    def pattern_sequence_file_url(cls, v):
        pattern = re.compile(
            r"^https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)$"
        )
        if isinstance(v, list):
            for element in v:
                if not pattern.match(element):
                    raise ValueError(f"Invalid sequence_file_url format: {element}")
        elif isinstance(v, str):
            if not pattern.match(v):
                raise ValueError(f"Invalid sequence_file_url format: {v}")
        return v


class BenchlingUrlSource(RepositoryIdSource):
    """
    Represents the source of a sequence that is identified by a Benchling URL
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "from_schema": "https://w3id.org/genestorian/ShareYourCloning_LinkML",
            "slot_usage": {
                "repository_id": {
                    "description": "The url of the gb file " "associated with the sequence",
                    "name": "repository_id",
                    "pattern": "^https:\\/\\/benchling\\.com\\/.+\\.gb$",
                }
            },
        }
    )

    repository_id: str = Field(
        ...,
        description="""The url of the gb file associated with the sequence""",
        json_schema_extra={"linkml_meta": {"alias": "repository_id", "domain_of": ["RepositoryIdSource"]}},
    )
    repository_name: RepositoryName = Field(
        ..., json_schema_extra={"linkml_meta": {"alias": "repository_name", "domain_of": ["RepositoryIdSource"]}}
    )
    input: Optional[List[int]] = Field(
        None,
        description="""The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.""",
        json_schema_extra={"linkml_meta": {"alias": "input", "domain_of": ["Source"]}},
    )
    output: Optional[int] = Field(
        None,
        description="""Identifier of the sequence that is the output of this source.""",
        json_schema_extra={"linkml_meta": {"alias": "output", "domain_of": ["Source"]}},
    )
    type: Literal["BenchlingUrlSource"] = Field(
        "BenchlingUrlSource",
        description="""The type of the source""",
        json_schema_extra={
            "linkml_meta": {"alias": "type", "designates_type": True, "domain_of": ["Sequence", "Source"]}
        },
    )
    output_name: Optional[str] = Field(
        None,
        description="""Used to specify the name of the output sequence""",
        json_schema_extra={"linkml_meta": {"alias": "output_name", "domain_of": ["Source"]}},
    )
    id: int = Field(
        ...,
        description="""A unique identifier for a thing""",
        json_schema_extra={
            "linkml_meta": {"alias": "id", "domain_of": ["NamedThing", "Sequence"], "slot_uri": "schema:identifier"}
        },
    )

    @field_validator("repository_id")
    def pattern_repository_id(cls, v):
        pattern = re.compile(r"^https:\/\/benchling\.com\/.+\.gb$")
        if isinstance(v, list):
            for element in v:
                if not pattern.match(element):
                    raise ValueError(f"Invalid repository_id format: {element}")
        elif isinstance(v, str):
            if not pattern.match(v):
                raise ValueError(f"Invalid repository_id format: {v}")
        return v


class GenomeCoordinatesSource(Source):
    """
    Represents the source of a sequence that is identified by genome coordinates, requested from NCBI
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {"from_schema": "https://w3id.org/genestorian/ShareYourCloning_LinkML"}
    )

    assembly_accession: Optional[str] = Field(
        None,
        description="""The accession of the assembly""",
        json_schema_extra={"linkml_meta": {"alias": "assembly_accession", "domain_of": ["GenomeCoordinatesSource"]}},
    )
    sequence_accession: str = Field(
        ...,
        description="""The accession of the sequence""",
        json_schema_extra={"linkml_meta": {"alias": "sequence_accession", "domain_of": ["GenomeCoordinatesSource"]}},
    )
    locus_tag: Optional[str] = Field(
        None,
        description="""The locus tag of the sequence""",
        json_schema_extra={"linkml_meta": {"alias": "locus_tag", "domain_of": ["GenomeCoordinatesSource"]}},
    )
    gene_id: Optional[int] = Field(
        None,
        description="""The gene id of the sequence""",
        json_schema_extra={"linkml_meta": {"alias": "gene_id", "domain_of": ["GenomeCoordinatesSource"]}},
    )
    start: int = Field(
        ...,
        description="""The starting coordinate (1-based) of the sequence in the sequence accession""",
        json_schema_extra={
            "linkml_meta": {"alias": "start", "domain_of": ["GenomeCoordinatesSource", "SimpleSequenceLocation"]}
        },
    )
    end: int = Field(
        ...,
        description="""The ending coordinate (1-based) of the sequence in the sequence accession""",
        json_schema_extra={
            "linkml_meta": {"alias": "end", "domain_of": ["GenomeCoordinatesSource", "SimpleSequenceLocation"]}
        },
    )
    strand: int = Field(
        ...,
        description="""The strand of the sequence in the sequence accession, should be 1 or -1""",
        json_schema_extra={
            "linkml_meta": {"alias": "strand", "domain_of": ["GenomeCoordinatesSource", "SimpleSequenceLocation"]}
        },
    )
    input: Optional[List[int]] = Field(
        None,
        description="""The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.""",
        json_schema_extra={"linkml_meta": {"alias": "input", "domain_of": ["Source"]}},
    )
    output: Optional[int] = Field(
        None,
        description="""Identifier of the sequence that is the output of this source.""",
        json_schema_extra={"linkml_meta": {"alias": "output", "domain_of": ["Source"]}},
    )
    type: Literal["GenomeCoordinatesSource"] = Field(
        "GenomeCoordinatesSource",
        description="""The type of the source""",
        json_schema_extra={
            "linkml_meta": {"alias": "type", "designates_type": True, "domain_of": ["Sequence", "Source"]}
        },
    )
    output_name: Optional[str] = Field(
        None,
        description="""Used to specify the name of the output sequence""",
        json_schema_extra={"linkml_meta": {"alias": "output_name", "domain_of": ["Source"]}},
    )
    id: int = Field(
        ...,
        description="""A unique identifier for a thing""",
        json_schema_extra={
            "linkml_meta": {"alias": "id", "domain_of": ["NamedThing", "Sequence"], "slot_uri": "schema:identifier"}
        },
    )


class SequenceCutSource(Source):
    """
    Represents the source of a sequence that is a subfragment of another sequence, generated by sequence cutting.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {"from_schema": "https://w3id.org/genestorian/ShareYourCloning_LinkML"}
    )

    left_edge: Optional[SequenceCut] = Field(
        None,
        json_schema_extra={
            "linkml_meta": {
                "alias": "left_edge",
                "domain_of": ["SequenceCutSource", "RestrictionEnzymeDigestionSource"],
            }
        },
    )
    right_edge: Optional[SequenceCut] = Field(
        None,
        json_schema_extra={
            "linkml_meta": {
                "alias": "right_edge",
                "domain_of": ["SequenceCutSource", "RestrictionEnzymeDigestionSource"],
            }
        },
    )
    input: Optional[List[int]] = Field(
        None,
        description="""The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.""",
        json_schema_extra={"linkml_meta": {"alias": "input", "domain_of": ["Source"]}},
    )
    output: Optional[int] = Field(
        None,
        description="""Identifier of the sequence that is the output of this source.""",
        json_schema_extra={"linkml_meta": {"alias": "output", "domain_of": ["Source"]}},
    )
    type: Literal["SequenceCutSource"] = Field(
        "SequenceCutSource",
        description="""The type of the source""",
        json_schema_extra={
            "linkml_meta": {"alias": "type", "designates_type": True, "domain_of": ["Sequence", "Source"]}
        },
    )
    output_name: Optional[str] = Field(
        None,
        description="""Used to specify the name of the output sequence""",
        json_schema_extra={"linkml_meta": {"alias": "output_name", "domain_of": ["Source"]}},
    )
    id: int = Field(
        ...,
        description="""A unique identifier for a thing""",
        json_schema_extra={
            "linkml_meta": {"alias": "id", "domain_of": ["NamedThing", "Sequence"], "slot_uri": "schema:identifier"}
        },
    )


class RestrictionEnzymeDigestionSource(SequenceCutSource):
    """
    Represents the source of a sequence that is a subfragment of another sequence, generated by sequence cutting using restriction enzymes.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {"from_schema": "https://w3id.org/genestorian/ShareYourCloning_LinkML"}
    )

    left_edge: Optional[RestrictionSequenceCut] = Field(
        None,
        json_schema_extra={
            "linkml_meta": {
                "alias": "left_edge",
                "domain_of": ["SequenceCutSource", "RestrictionEnzymeDigestionSource"],
            }
        },
    )
    right_edge: Optional[RestrictionSequenceCut] = Field(
        None,
        json_schema_extra={
            "linkml_meta": {
                "alias": "right_edge",
                "domain_of": ["SequenceCutSource", "RestrictionEnzymeDigestionSource"],
            }
        },
    )
    input: Optional[List[int]] = Field(
        None,
        description="""The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.""",
        json_schema_extra={"linkml_meta": {"alias": "input", "domain_of": ["Source"]}},
    )
    output: Optional[int] = Field(
        None,
        description="""Identifier of the sequence that is the output of this source.""",
        json_schema_extra={"linkml_meta": {"alias": "output", "domain_of": ["Source"]}},
    )
    type: Literal["RestrictionEnzymeDigestionSource"] = Field(
        "RestrictionEnzymeDigestionSource",
        description="""The type of the source""",
        json_schema_extra={
            "linkml_meta": {"alias": "type", "designates_type": True, "domain_of": ["Sequence", "Source"]}
        },
    )
    output_name: Optional[str] = Field(
        None,
        description="""Used to specify the name of the output sequence""",
        json_schema_extra={"linkml_meta": {"alias": "output_name", "domain_of": ["Source"]}},
    )
    id: int = Field(
        ...,
        description="""A unique identifier for a thing""",
        json_schema_extra={
            "linkml_meta": {"alias": "id", "domain_of": ["NamedThing", "Sequence"], "slot_uri": "schema:identifier"}
        },
    )


class SimpleSequenceLocation(ConfiguredBaseModel):
    """
    Represents a location within a sequence, for now support for ranges only
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {"from_schema": "https://w3id.org/genestorian/ShareYourCloning_LinkML"}
    )

    start: int = Field(
        ...,
        description="""The starting coordinate (1-based) of the location""",
        json_schema_extra={
            "linkml_meta": {"alias": "start", "domain_of": ["GenomeCoordinatesSource", "SimpleSequenceLocation"]}
        },
    )
    end: int = Field(
        ...,
        description="""The ending coordinate (1-based) of the location""",
        json_schema_extra={
            "linkml_meta": {"alias": "end", "domain_of": ["GenomeCoordinatesSource", "SimpleSequenceLocation"]}
        },
    )
    strand: Optional[int] = Field(
        None,
        description="""The strand of the location, should be 1 or -1 or null""",
        json_schema_extra={
            "linkml_meta": {"alias": "strand", "domain_of": ["GenomeCoordinatesSource", "SimpleSequenceLocation"]}
        },
    )


class AssemblyFragment(ConfiguredBaseModel):
    """
    Represents a fragment in an assembly
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {"from_schema": "https://w3id.org/genestorian/ShareYourCloning_LinkML"}
    )

    sequence: int = Field(
        ..., json_schema_extra={"linkml_meta": {"alias": "sequence", "domain_of": ["Primer", "AssemblyFragment"]}}
    )
    left_location: SimpleSequenceLocation = Field(
        ..., json_schema_extra={"linkml_meta": {"alias": "left_location", "domain_of": ["AssemblyFragment"]}}
    )
    right_location: SimpleSequenceLocation = Field(
        ..., json_schema_extra={"linkml_meta": {"alias": "right_location", "domain_of": ["AssemblyFragment"]}}
    )
    reverse_complemented: bool = Field(
        ...,
        description="""Whether the sequence is reverse complemented in the assembly""",
        json_schema_extra={"linkml_meta": {"alias": "reverse_complemented", "domain_of": ["AssemblyFragment"]}},
    )


class AssemblySource(Source):
    """
    Represents the source of a sequence that is an assembly of other sequences
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {"from_schema": "https://w3id.org/genestorian/ShareYourCloning_LinkML"}
    )

    circular: Optional[bool] = Field(
        None,
        description="""Whether the assembly is circular or not""",
        json_schema_extra={
            "linkml_meta": {"alias": "circular", "domain_of": ["ManuallyTypedSource", "AssemblySource"]}
        },
    )
    assembly: List[AssemblyFragment] = Field(
        ...,
        description="""A list of the fragments that are assembled, in order""",
        json_schema_extra={"linkml_meta": {"alias": "assembly", "domain_of": ["AssemblySource"]}},
    )
    input: Optional[List[int]] = Field(
        None,
        description="""The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.""",
        json_schema_extra={"linkml_meta": {"alias": "input", "domain_of": ["Source"]}},
    )
    output: Optional[int] = Field(
        None,
        description="""Identifier of the sequence that is the output of this source.""",
        json_schema_extra={"linkml_meta": {"alias": "output", "domain_of": ["Source"]}},
    )
    type: Literal["AssemblySource"] = Field(
        "AssemblySource",
        description="""The type of the source""",
        json_schema_extra={
            "linkml_meta": {"alias": "type", "designates_type": True, "domain_of": ["Sequence", "Source"]}
        },
    )
    output_name: Optional[str] = Field(
        None,
        description="""Used to specify the name of the output sequence""",
        json_schema_extra={"linkml_meta": {"alias": "output_name", "domain_of": ["Source"]}},
    )
    id: int = Field(
        ...,
        description="""A unique identifier for a thing""",
        json_schema_extra={
            "linkml_meta": {"alias": "id", "domain_of": ["NamedThing", "Sequence"], "slot_uri": "schema:identifier"}
        },
    )


class PCRSource(AssemblySource):
    """
    Represents the source of a sequence that is generated by PCR
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {"from_schema": "https://w3id.org/genestorian/ShareYourCloning_LinkML"}
    )

    circular: Optional[bool] = Field(
        None,
        description="""Whether the assembly is circular or not""",
        json_schema_extra={
            "linkml_meta": {"alias": "circular", "domain_of": ["ManuallyTypedSource", "AssemblySource"]}
        },
    )
    assembly: List[AssemblyFragment] = Field(
        ...,
        description="""A list of the fragments that are assembled, in order""",
        json_schema_extra={"linkml_meta": {"alias": "assembly", "domain_of": ["AssemblySource"]}},
    )
    input: Optional[List[int]] = Field(
        None,
        description="""The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.""",
        json_schema_extra={"linkml_meta": {"alias": "input", "domain_of": ["Source"]}},
    )
    output: Optional[int] = Field(
        None,
        description="""Identifier of the sequence that is the output of this source.""",
        json_schema_extra={"linkml_meta": {"alias": "output", "domain_of": ["Source"]}},
    )
    type: Literal["PCRSource"] = Field(
        "PCRSource",
        description="""The type of the source""",
        json_schema_extra={
            "linkml_meta": {"alias": "type", "designates_type": True, "domain_of": ["Sequence", "Source"]}
        },
    )
    output_name: Optional[str] = Field(
        None,
        description="""Used to specify the name of the output sequence""",
        json_schema_extra={"linkml_meta": {"alias": "output_name", "domain_of": ["Source"]}},
    )
    id: int = Field(
        ...,
        description="""A unique identifier for a thing""",
        json_schema_extra={
            "linkml_meta": {"alias": "id", "domain_of": ["NamedThing", "Sequence"], "slot_uri": "schema:identifier"}
        },
    )


class LigationSource(AssemblySource):
    """
    Represents the source of a sequence that is generated by ligation with sticky or blunt ends.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {"from_schema": "https://w3id.org/genestorian/ShareYourCloning_LinkML"}
    )

    circular: Optional[bool] = Field(
        None,
        description="""Whether the assembly is circular or not""",
        json_schema_extra={
            "linkml_meta": {"alias": "circular", "domain_of": ["ManuallyTypedSource", "AssemblySource"]}
        },
    )
    assembly: List[AssemblyFragment] = Field(
        ...,
        description="""A list of the fragments that are assembled, in order""",
        json_schema_extra={"linkml_meta": {"alias": "assembly", "domain_of": ["AssemblySource"]}},
    )
    input: Optional[List[int]] = Field(
        None,
        description="""The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.""",
        json_schema_extra={"linkml_meta": {"alias": "input", "domain_of": ["Source"]}},
    )
    output: Optional[int] = Field(
        None,
        description="""Identifier of the sequence that is the output of this source.""",
        json_schema_extra={"linkml_meta": {"alias": "output", "domain_of": ["Source"]}},
    )
    type: Literal["LigationSource"] = Field(
        "LigationSource",
        description="""The type of the source""",
        json_schema_extra={
            "linkml_meta": {"alias": "type", "designates_type": True, "domain_of": ["Sequence", "Source"]}
        },
    )
    output_name: Optional[str] = Field(
        None,
        description="""Used to specify the name of the output sequence""",
        json_schema_extra={"linkml_meta": {"alias": "output_name", "domain_of": ["Source"]}},
    )
    id: int = Field(
        ...,
        description="""A unique identifier for a thing""",
        json_schema_extra={
            "linkml_meta": {"alias": "id", "domain_of": ["NamedThing", "Sequence"], "slot_uri": "schema:identifier"}
        },
    )


class HomologousRecombinationSource(AssemblySource):
    """
    Represents the source of a sequence that is generated by homologous recombination
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {"from_schema": "https://w3id.org/genestorian/ShareYourCloning_LinkML"}
    )

    circular: Optional[bool] = Field(
        None,
        description="""Whether the assembly is circular or not""",
        json_schema_extra={
            "linkml_meta": {"alias": "circular", "domain_of": ["ManuallyTypedSource", "AssemblySource"]}
        },
    )
    assembly: List[AssemblyFragment] = Field(
        ...,
        description="""A list of the fragments that are assembled, in order""",
        json_schema_extra={"linkml_meta": {"alias": "assembly", "domain_of": ["AssemblySource"]}},
    )
    input: Optional[List[int]] = Field(
        None,
        description="""The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.""",
        json_schema_extra={"linkml_meta": {"alias": "input", "domain_of": ["Source"]}},
    )
    output: Optional[int] = Field(
        None,
        description="""Identifier of the sequence that is the output of this source.""",
        json_schema_extra={"linkml_meta": {"alias": "output", "domain_of": ["Source"]}},
    )
    type: Literal["HomologousRecombinationSource"] = Field(
        "HomologousRecombinationSource",
        description="""The type of the source""",
        json_schema_extra={
            "linkml_meta": {"alias": "type", "designates_type": True, "domain_of": ["Sequence", "Source"]}
        },
    )
    output_name: Optional[str] = Field(
        None,
        description="""Used to specify the name of the output sequence""",
        json_schema_extra={"linkml_meta": {"alias": "output_name", "domain_of": ["Source"]}},
    )
    id: int = Field(
        ...,
        description="""A unique identifier for a thing""",
        json_schema_extra={
            "linkml_meta": {"alias": "id", "domain_of": ["NamedThing", "Sequence"], "slot_uri": "schema:identifier"}
        },
    )


class GibsonAssemblySource(AssemblySource):
    """
    Represents the source of a sequence that is generated by Gibson assembly
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {"from_schema": "https://w3id.org/genestorian/ShareYourCloning_LinkML"}
    )

    circular: Optional[bool] = Field(
        None,
        description="""Whether the assembly is circular or not""",
        json_schema_extra={
            "linkml_meta": {"alias": "circular", "domain_of": ["ManuallyTypedSource", "AssemblySource"]}
        },
    )
    assembly: List[AssemblyFragment] = Field(
        ...,
        description="""A list of the fragments that are assembled, in order""",
        json_schema_extra={"linkml_meta": {"alias": "assembly", "domain_of": ["AssemblySource"]}},
    )
    input: Optional[List[int]] = Field(
        None,
        description="""The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.""",
        json_schema_extra={"linkml_meta": {"alias": "input", "domain_of": ["Source"]}},
    )
    output: Optional[int] = Field(
        None,
        description="""Identifier of the sequence that is the output of this source.""",
        json_schema_extra={"linkml_meta": {"alias": "output", "domain_of": ["Source"]}},
    )
    type: Literal["GibsonAssemblySource"] = Field(
        "GibsonAssemblySource",
        description="""The type of the source""",
        json_schema_extra={
            "linkml_meta": {"alias": "type", "designates_type": True, "domain_of": ["Sequence", "Source"]}
        },
    )
    output_name: Optional[str] = Field(
        None,
        description="""Used to specify the name of the output sequence""",
        json_schema_extra={"linkml_meta": {"alias": "output_name", "domain_of": ["Source"]}},
    )
    id: int = Field(
        ...,
        description="""A unique identifier for a thing""",
        json_schema_extra={
            "linkml_meta": {"alias": "id", "domain_of": ["NamedThing", "Sequence"], "slot_uri": "schema:identifier"}
        },
    )


class OverlapExtensionPCRLigationSource(AssemblySource):
    """
    Represents the source of a sequence that is generated by ligation of PCR products as part of overlap extension PCR. Algorithmically equivalent to Gibson assembly.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {"from_schema": "https://w3id.org/genestorian/ShareYourCloning_LinkML"}
    )

    circular: Optional[bool] = Field(
        None,
        description="""Whether the assembly is circular or not""",
        json_schema_extra={
            "linkml_meta": {"alias": "circular", "domain_of": ["ManuallyTypedSource", "AssemblySource"]}
        },
    )
    assembly: List[AssemblyFragment] = Field(
        ...,
        description="""A list of the fragments that are assembled, in order""",
        json_schema_extra={"linkml_meta": {"alias": "assembly", "domain_of": ["AssemblySource"]}},
    )
    input: Optional[List[int]] = Field(
        None,
        description="""The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.""",
        json_schema_extra={"linkml_meta": {"alias": "input", "domain_of": ["Source"]}},
    )
    output: Optional[int] = Field(
        None,
        description="""Identifier of the sequence that is the output of this source.""",
        json_schema_extra={"linkml_meta": {"alias": "output", "domain_of": ["Source"]}},
    )
    type: Literal["OverlapExtensionPCRLigationSource"] = Field(
        "OverlapExtensionPCRLigationSource",
        description="""The type of the source""",
        json_schema_extra={
            "linkml_meta": {"alias": "type", "designates_type": True, "domain_of": ["Sequence", "Source"]}
        },
    )
    output_name: Optional[str] = Field(
        None,
        description="""Used to specify the name of the output sequence""",
        json_schema_extra={"linkml_meta": {"alias": "output_name", "domain_of": ["Source"]}},
    )
    id: int = Field(
        ...,
        description="""A unique identifier for a thing""",
        json_schema_extra={
            "linkml_meta": {"alias": "id", "domain_of": ["NamedThing", "Sequence"], "slot_uri": "schema:identifier"}
        },
    )


class RestrictionAndLigationSource(AssemblySource):
    """
    Represents the source of a sequence that is generated by restriction and ligation
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "from_schema": "https://w3id.org/genestorian/ShareYourCloning_LinkML",
            "slot_usage": {"restriction_enzymes": {"name": "restriction_enzymes", "required": True}},
        }
    )

    restriction_enzymes: List[str] = Field(
        ...,
        json_schema_extra={
            "linkml_meta": {
                "alias": "restriction_enzymes",
                "domain_of": ["RestrictionAndLigationSource"],
                "exact_mappings": ["OBI:0000732"],
            }
        },
    )
    circular: Optional[bool] = Field(
        None,
        description="""Whether the assembly is circular or not""",
        json_schema_extra={
            "linkml_meta": {"alias": "circular", "domain_of": ["ManuallyTypedSource", "AssemblySource"]}
        },
    )
    assembly: List[AssemblyFragment] = Field(
        ...,
        description="""A list of the fragments that are assembled, in order""",
        json_schema_extra={"linkml_meta": {"alias": "assembly", "domain_of": ["AssemblySource"]}},
    )
    input: Optional[List[int]] = Field(
        None,
        description="""The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.""",
        json_schema_extra={"linkml_meta": {"alias": "input", "domain_of": ["Source"]}},
    )
    output: Optional[int] = Field(
        None,
        description="""Identifier of the sequence that is the output of this source.""",
        json_schema_extra={"linkml_meta": {"alias": "output", "domain_of": ["Source"]}},
    )
    type: Literal["RestrictionAndLigationSource"] = Field(
        "RestrictionAndLigationSource",
        description="""The type of the source""",
        json_schema_extra={
            "linkml_meta": {"alias": "type", "designates_type": True, "domain_of": ["Sequence", "Source"]}
        },
    )
    output_name: Optional[str] = Field(
        None,
        description="""Used to specify the name of the output sequence""",
        json_schema_extra={"linkml_meta": {"alias": "output_name", "domain_of": ["Source"]}},
    )
    id: int = Field(
        ...,
        description="""A unique identifier for a thing""",
        json_schema_extra={
            "linkml_meta": {"alias": "id", "domain_of": ["NamedThing", "Sequence"], "slot_uri": "schema:identifier"}
        },
    )


class CRISPRSource(HomologousRecombinationSource):
    """
    Represents the source of a sequence that is generated by CRISPR
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {"from_schema": "https://w3id.org/genestorian/ShareYourCloning_LinkML"}
    )

    guides: List[int] = Field(
        ...,
        description="""The guide RNAs used in the CRISPR""",
        json_schema_extra={"linkml_meta": {"alias": "guides", "domain_of": ["CRISPRSource"]}},
    )
    circular: Optional[bool] = Field(
        None,
        description="""Whether the assembly is circular or not""",
        json_schema_extra={
            "linkml_meta": {"alias": "circular", "domain_of": ["ManuallyTypedSource", "AssemblySource"]}
        },
    )
    assembly: List[AssemblyFragment] = Field(
        ...,
        description="""A list of the fragments that are assembled, in order""",
        json_schema_extra={"linkml_meta": {"alias": "assembly", "domain_of": ["AssemblySource"]}},
    )
    input: Optional[List[int]] = Field(
        None,
        description="""The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.""",
        json_schema_extra={"linkml_meta": {"alias": "input", "domain_of": ["Source"]}},
    )
    output: Optional[int] = Field(
        None,
        description="""Identifier of the sequence that is the output of this source.""",
        json_schema_extra={"linkml_meta": {"alias": "output", "domain_of": ["Source"]}},
    )
    type: Literal["CRISPRSource"] = Field(
        "CRISPRSource",
        description="""The type of the source""",
        json_schema_extra={
            "linkml_meta": {"alias": "type", "designates_type": True, "domain_of": ["Sequence", "Source"]}
        },
    )
    output_name: Optional[str] = Field(
        None,
        description="""Used to specify the name of the output sequence""",
        json_schema_extra={"linkml_meta": {"alias": "output_name", "domain_of": ["Source"]}},
    )
    id: int = Field(
        ...,
        description="""A unique identifier for a thing""",
        json_schema_extra={
            "linkml_meta": {"alias": "id", "domain_of": ["NamedThing", "Sequence"], "slot_uri": "schema:identifier"}
        },
    )


class OligoHybridizationSource(Source):
    """
    Represents the source of a sequence that is generated by oligo hybridization
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {"from_schema": "https://w3id.org/genestorian/ShareYourCloning_LinkML"}
    )

    overhang_crick_3prime: Optional[int] = Field(
        None,
        description="""Taken from pydna's `dseq::ovhg`An integer describing the length of the crick strand overhang in the 5' of the molecule, or 3' of the crick strand""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "overhang_crick_3prime",
                "domain_of": ["TextFileSequence", "ManuallyTypedSource", "OligoHybridizationSource"],
            }
        },
    )
    forward_oligo: int = Field(
        ...,
        description="""The forward oligo used in the hybridization""",
        json_schema_extra={"linkml_meta": {"alias": "forward_oligo", "domain_of": ["OligoHybridizationSource"]}},
    )
    reverse_oligo: int = Field(
        ...,
        description="""The reverse oligo used in the hybridization""",
        json_schema_extra={"linkml_meta": {"alias": "reverse_oligo", "domain_of": ["OligoHybridizationSource"]}},
    )
    input: Optional[List[int]] = Field(
        None,
        description="""The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.""",
        json_schema_extra={"linkml_meta": {"alias": "input", "domain_of": ["Source"]}},
    )
    output: Optional[int] = Field(
        None,
        description="""Identifier of the sequence that is the output of this source.""",
        json_schema_extra={"linkml_meta": {"alias": "output", "domain_of": ["Source"]}},
    )
    type: Literal["OligoHybridizationSource"] = Field(
        "OligoHybridizationSource",
        description="""The type of the source""",
        json_schema_extra={
            "linkml_meta": {"alias": "type", "designates_type": True, "domain_of": ["Sequence", "Source"]}
        },
    )
    output_name: Optional[str] = Field(
        None,
        description="""Used to specify the name of the output sequence""",
        json_schema_extra={"linkml_meta": {"alias": "output_name", "domain_of": ["Source"]}},
    )
    id: int = Field(
        ...,
        description="""A unique identifier for a thing""",
        json_schema_extra={
            "linkml_meta": {"alias": "id", "domain_of": ["NamedThing", "Sequence"], "slot_uri": "schema:identifier"}
        },
    )


class PolymeraseExtensionSource(Source):
    """
    Represents the source of a sequence that is generated by polymerase extension
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {"from_schema": "https://w3id.org/genestorian/ShareYourCloning_LinkML"}
    )

    input: Optional[List[int]] = Field(
        None,
        description="""The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.""",
        json_schema_extra={"linkml_meta": {"alias": "input", "domain_of": ["Source"]}},
    )
    output: Optional[int] = Field(
        None,
        description="""Identifier of the sequence that is the output of this source.""",
        json_schema_extra={"linkml_meta": {"alias": "output", "domain_of": ["Source"]}},
    )
    type: Literal["PolymeraseExtensionSource"] = Field(
        "PolymeraseExtensionSource",
        description="""The type of the source""",
        json_schema_extra={
            "linkml_meta": {"alias": "type", "designates_type": True, "domain_of": ["Sequence", "Source"]}
        },
    )
    output_name: Optional[str] = Field(
        None,
        description="""Used to specify the name of the output sequence""",
        json_schema_extra={"linkml_meta": {"alias": "output_name", "domain_of": ["Source"]}},
    )
    id: int = Field(
        ...,
        description="""A unique identifier for a thing""",
        json_schema_extra={
            "linkml_meta": {"alias": "id", "domain_of": ["NamedThing", "Sequence"], "slot_uri": "schema:identifier"}
        },
    )


class CloningStrategy(ConfiguredBaseModel):
    """
    Represents a cloning strategy
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {"from_schema": "https://w3id.org/genestorian/ShareYourCloning_LinkML"}
    )

    sequences: List[Union[Sequence, TextFileSequence, Primer]] = Field(
        ...,
        description="""The sequences that are used in the cloning strategy""",
        json_schema_extra={"linkml_meta": {"alias": "sequences", "domain_of": ["CloningStrategy"]}},
    )
    sources: List[
        Union[
            Source,
            ManuallyTypedSource,
            UploadedFileSource,
            RepositoryIdSource,
            GenomeCoordinatesSource,
            SequenceCutSource,
            AssemblySource,
            OligoHybridizationSource,
            PolymeraseExtensionSource,
            PCRSource,
            LigationSource,
            HomologousRecombinationSource,
            GibsonAssemblySource,
            OverlapExtensionPCRLigationSource,
            RestrictionAndLigationSource,
            CRISPRSource,
            RestrictionEnzymeDigestionSource,
            AddGeneIdSource,
            BenchlingUrlSource,
        ]
    ] = Field(
        ...,
        description="""The sources of the sequences that are used in the cloning strategy""",
        json_schema_extra={"linkml_meta": {"alias": "sources", "domain_of": ["CloningStrategy"]}},
    )
    primers: Optional[List[Primer]] = Field(
        None,
        description="""The primers that are used in the cloning strategy""",
        json_schema_extra={"linkml_meta": {"alias": "primers", "domain_of": ["CloningStrategy"]}},
    )
    description: Optional[str] = Field(
        None,
        description="""A description of the cloning strategy""",
        json_schema_extra={"linkml_meta": {"alias": "description", "domain_of": ["CloningStrategy"]}},
    )


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
NamedThing.model_rebuild()
Sequence.model_rebuild()
TextFileSequence.model_rebuild()
Primer.model_rebuild()
SequenceCut.model_rebuild()
RestrictionSequenceCut.model_rebuild()
Source.model_rebuild()
ManuallyTypedSource.model_rebuild()
UploadedFileSource.model_rebuild()
RepositoryIdSource.model_rebuild()
AddGeneIdSource.model_rebuild()
BenchlingUrlSource.model_rebuild()
GenomeCoordinatesSource.model_rebuild()
SequenceCutSource.model_rebuild()
RestrictionEnzymeDigestionSource.model_rebuild()
SimpleSequenceLocation.model_rebuild()
AssemblyFragment.model_rebuild()
AssemblySource.model_rebuild()
PCRSource.model_rebuild()
LigationSource.model_rebuild()
HomologousRecombinationSource.model_rebuild()
GibsonAssemblySource.model_rebuild()
OverlapExtensionPCRLigationSource.model_rebuild()
RestrictionAndLigationSource.model_rebuild()
CRISPRSource.model_rebuild()
OligoHybridizationSource.model_rebuild()
PolymeraseExtensionSource.model_rebuild()
CloningStrategy.model_rebuild()
