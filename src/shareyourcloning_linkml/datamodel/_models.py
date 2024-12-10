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
    # SnapGene plasmid library
    snapgene = "snapgene"
    # Euroscarf (plasmids only)
    euroscarf = "euroscarf"
    # iGEM collection
    igem = "igem"


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


class GatewayReactionType(str, Enum):
    # LR reaction
    LR = "LR"
    # BP reaction
    BP = "BP"


class AnnotationTool(str, Enum):
    plannotate = "plannotate"


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
        description="""Designates the class""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "designates_type": True,
                "domain_of": ["Sequence", "Source", "AnnotationReport"],
            }
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
        description="""Designates the class""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "designates_type": True,
                "domain_of": ["Sequence", "Source", "AnnotationReport"],
            }
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
        None,
        json_schema_extra={
            "linkml_meta": {
                "alias": "sequence",
                "domain_of": ["Primer", "AssemblyFragment", "PlannotateAnnotationReport"],
            }
        },
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
        description="""Designates the class""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "designates_type": True,
                "domain_of": ["Sequence", "Source", "AnnotationReport"],
            }
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
        description="""Designates the class""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "designates_type": True,
                "domain_of": ["Sequence", "Source", "AnnotationReport"],
            }
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
        description="""Designates the class""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "designates_type": True,
                "domain_of": ["Sequence", "Source", "AnnotationReport"],
            }
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
        description="""Designates the class""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "designates_type": True,
                "domain_of": ["Sequence", "Source", "AnnotationReport"],
            }
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
        description="""Designates the class""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "designates_type": True,
                "domain_of": ["Sequence", "Source", "AnnotationReport"],
            }
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
        json_schema_extra={
            "linkml_meta": {"alias": "sequence_file_url", "domain_of": ["AddGeneIdSource", "IGEMSource"]}
        },
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
        description="""Designates the class""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "designates_type": True,
                "domain_of": ["Sequence", "Source", "AnnotationReport"],
            }
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
        description="""Designates the class""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "designates_type": True,
                "domain_of": ["Sequence", "Source", "AnnotationReport"],
            }
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


class SnapGenePlasmidSource(RepositoryIdSource):
    """
    Represents the source of a sequence from the SnapGene plasmid library identified by a SnapGene subpath of https://www.snapgene.com/plasmids/
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "from_schema": "https://w3id.org/genestorian/ShareYourCloning_LinkML",
            "slot_usage": {
                "repository_id": {
                    "description": "The subpath of the plasmid "
                    "in the SnapGene plasmid "
                    "library. Requesting the "
                    "plasmid is possible with "
                    "https://www.snapgene.com/local/fetch.php?set={category_path}&plasmid={plasmid['subpath']} "
                    "where category_path is the "
                    "left part of the subpath "
                    "before the first / and "
                    "plasmid is the subpath after "
                    "the /.",
                    "name": "repository_id",
                    "pattern": "^.+\\/.+$",
                }
            },
        }
    )

    repository_id: str = Field(
        ...,
        description="""The subpath of the plasmid in the SnapGene plasmid library. Requesting the plasmid is possible with https://www.snapgene.com/local/fetch.php?set={category_path}&plasmid={plasmid['subpath']} where category_path is the left part of the subpath before the first / and plasmid is the subpath after the /.""",
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
    type: Literal["SnapGenePlasmidSource"] = Field(
        "SnapGenePlasmidSource",
        description="""Designates the class""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "designates_type": True,
                "domain_of": ["Sequence", "Source", "AnnotationReport"],
            }
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
        pattern = re.compile(r"^.+\/.+$")
        if isinstance(v, list):
            for element in v:
                if not pattern.match(element):
                    raise ValueError(f"Invalid repository_id format: {element}")
        elif isinstance(v, str):
            if not pattern.match(v):
                raise ValueError(f"Invalid repository_id format: {v}")
        return v


class EuroscarfSource(RepositoryIdSource):
    """
    Represents the source of a sequence from the Euroscarf plasmid library
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "from_schema": "https://w3id.org/genestorian/ShareYourCloning_LinkML",
            "slot_usage": {
                "repository_id": {
                    "description": "The id of the plasmid in the " "Euroscarf plasmid library",
                    "name": "repository_id",
                    "pattern": "^P\\d+$",
                }
            },
        }
    )

    repository_id: str = Field(
        ...,
        description="""The id of the plasmid in the Euroscarf plasmid library""",
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
    type: Literal["EuroscarfSource"] = Field(
        "EuroscarfSource",
        description="""Designates the class""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "designates_type": True,
                "domain_of": ["Sequence", "Source", "AnnotationReport"],
            }
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
        pattern = re.compile(r"^P\d+$")
        if isinstance(v, list):
            for element in v:
                if not pattern.match(element):
                    raise ValueError(f"Invalid repository_id format: {element}")
        elif isinstance(v, str):
            if not pattern.match(v):
                raise ValueError(f"Invalid repository_id format: {v}")
        return v


class IGEMSource(RepositoryIdSource):
    """
    Represents the source of a sequence from an iGEM collection
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "from_schema": "https://w3id.org/genestorian/ShareYourCloning_LinkML",
            "slot_usage": {
                "repository_id": {
                    "description": "The unique identifier of the "
                    "sequence in the iGEM "
                    "collection (for now, "
                    "{part_id}-{plasmid_backbone})",
                    "name": "repository_id",
                },
                "sequence_file_url": {
                    "description": "The URL of the sequence " "file, for now github " "repository",
                    "name": "sequence_file_url",
                    "required": True,
                },
            },
        }
    )

    sequence_file_url: str = Field(
        ...,
        description="""The URL of the sequence file, for now github repository""",
        json_schema_extra={
            "linkml_meta": {"alias": "sequence_file_url", "domain_of": ["AddGeneIdSource", "IGEMSource"]}
        },
    )
    repository_id: str = Field(
        ...,
        description="""The unique identifier of the sequence in the iGEM collection (for now, {part_id}-{plasmid_backbone})""",
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
    type: Literal["IGEMSource"] = Field(
        "IGEMSource",
        description="""Designates the class""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "designates_type": True,
                "domain_of": ["Sequence", "Source", "AnnotationReport"],
            }
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
            "linkml_meta": {
                "alias": "strand",
                "domain_of": ["GenomeCoordinatesSource", "SimpleSequenceLocation", "PlannotateAnnotationReport"],
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
    type: Literal["GenomeCoordinatesSource"] = Field(
        "GenomeCoordinatesSource",
        description="""Designates the class""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "designates_type": True,
                "domain_of": ["Sequence", "Source", "AnnotationReport"],
            }
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
        description="""Designates the class""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "designates_type": True,
                "domain_of": ["Sequence", "Source", "AnnotationReport"],
            }
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
        description="""Designates the class""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "designates_type": True,
                "domain_of": ["Sequence", "Source", "AnnotationReport"],
            }
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
            "linkml_meta": {
                "alias": "strand",
                "domain_of": ["GenomeCoordinatesSource", "SimpleSequenceLocation", "PlannotateAnnotationReport"],
            }
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
        ...,
        json_schema_extra={
            "linkml_meta": {
                "alias": "sequence",
                "domain_of": ["Primer", "AssemblyFragment", "PlannotateAnnotationReport"],
            }
        },
    )
    left_location: Optional[SimpleSequenceLocation] = Field(
        None, json_schema_extra={"linkml_meta": {"alias": "left_location", "domain_of": ["AssemblyFragment"]}}
    )
    right_location: Optional[SimpleSequenceLocation] = Field(
        None, json_schema_extra={"linkml_meta": {"alias": "right_location", "domain_of": ["AssemblyFragment"]}}
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
        description="""Designates the class""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "designates_type": True,
                "domain_of": ["Sequence", "Source", "AnnotationReport"],
            }
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

    add_primer_features: Optional[bool] = Field(
        False,
        description="""Whether to add primer features to the PCR product""",
        json_schema_extra={
            "linkml_meta": {"alias": "add_primer_features", "domain_of": ["PCRSource"], "ifabsent": "boolean(false)"}
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
    type: Literal["PCRSource"] = Field(
        "PCRSource",
        description="""Designates the class""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "designates_type": True,
                "domain_of": ["Sequence", "Source", "AnnotationReport"],
            }
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
        description="""Designates the class""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "designates_type": True,
                "domain_of": ["Sequence", "Source", "AnnotationReport"],
            }
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
        description="""Designates the class""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "designates_type": True,
                "domain_of": ["Sequence", "Source", "AnnotationReport"],
            }
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
        description="""Designates the class""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "designates_type": True,
                "domain_of": ["Sequence", "Source", "AnnotationReport"],
            }
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


class InFusionSource(AssemblySource):
    """
    Represents the source of a sequence that is generated by In-Fusion cloning by Takara Bio
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
    type: Literal["InFusionSource"] = Field(
        "InFusionSource",
        description="""Designates the class""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "designates_type": True,
                "domain_of": ["Sequence", "Source", "AnnotationReport"],
            }
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
        description="""Designates the class""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "designates_type": True,
                "domain_of": ["Sequence", "Source", "AnnotationReport"],
            }
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
        description="""Designates the class""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "designates_type": True,
                "domain_of": ["Sequence", "Source", "AnnotationReport"],
            }
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


class GatewaySource(AssemblySource):
    """
    Represents the source of a sequence that is generated by Gateway cloning
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {"from_schema": "https://w3id.org/genestorian/ShareYourCloning_LinkML"}
    )

    reaction_type: GatewayReactionType = Field(
        ..., json_schema_extra={"linkml_meta": {"alias": "reaction_type", "domain_of": ["GatewaySource"]}}
    )
    greedy: Optional[bool] = Field(
        False,
        description="""Whether to use a greedy consensus sequence for att sites (see https://github.com/manulera/GateWayMine)""",
        json_schema_extra={
            "linkml_meta": {"alias": "greedy", "domain_of": ["GatewaySource"], "ifabsent": "boolean(false)"}
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
    type: Literal["GatewaySource"] = Field(
        "GatewaySource",
        description="""Designates the class""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "designates_type": True,
                "domain_of": ["Sequence", "Source", "AnnotationReport"],
            }
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
        description="""Designates the class""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "designates_type": True,
                "domain_of": ["Sequence", "Source", "AnnotationReport"],
            }
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
        description="""Designates the class""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "designates_type": True,
                "domain_of": ["Sequence", "Source", "AnnotationReport"],
            }
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
        description="""Designates the class""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "designates_type": True,
                "domain_of": ["Sequence", "Source", "AnnotationReport"],
            }
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
            AnnotationSource,
            PCRSource,
            LigationSource,
            HomologousRecombinationSource,
            GibsonAssemblySource,
            InFusionSource,
            OverlapExtensionPCRLigationSource,
            RestrictionAndLigationSource,
            GatewaySource,
            CRISPRSource,
            RestrictionEnzymeDigestionSource,
            AddGeneIdSource,
            BenchlingUrlSource,
            SnapGenePlasmidSource,
            EuroscarfSource,
            IGEMSource,
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


class AnnotationReport(ConfiguredBaseModel):
    """
    Represents a report of an annotation step
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {"from_schema": "https://w3id.org/genestorian/ShareYourCloning_LinkML"}
    )

    type: Literal["AnnotationReport"] = Field(
        "AnnotationReport",
        description="""Designates the class""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "designates_type": True,
                "domain_of": ["Sequence", "Source", "AnnotationReport"],
            }
        },
    )


class PlannotateAnnotationReport(AnnotationReport):
    """
    Represents a report of an annotation step using Plannotate
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {"from_schema": "https://w3id.org/genestorian/ShareYourCloning_LinkML"}
    )

    sseqid: Optional[str] = Field(
        None, json_schema_extra={"linkml_meta": {"alias": "sseqid", "domain_of": ["PlannotateAnnotationReport"]}}
    )
    start_location: Optional[int] = Field(
        None,
        json_schema_extra={"linkml_meta": {"alias": "start_location", "domain_of": ["PlannotateAnnotationReport"]}},
    )
    end_location: Optional[int] = Field(
        None, json_schema_extra={"linkml_meta": {"alias": "end_location", "domain_of": ["PlannotateAnnotationReport"]}}
    )
    strand: Optional[int] = Field(
        None,
        json_schema_extra={
            "linkml_meta": {
                "alias": "strand",
                "domain_of": ["GenomeCoordinatesSource", "SimpleSequenceLocation", "PlannotateAnnotationReport"],
            }
        },
    )
    percent_identity: Optional[float] = Field(
        None,
        json_schema_extra={"linkml_meta": {"alias": "percent_identity", "domain_of": ["PlannotateAnnotationReport"]}},
    )
    full_length_of_feature_in_db: Optional[int] = Field(
        None,
        json_schema_extra={
            "linkml_meta": {"alias": "full_length_of_feature_in_db", "domain_of": ["PlannotateAnnotationReport"]}
        },
    )
    length_of_found_feature: Optional[int] = Field(
        None,
        json_schema_extra={
            "linkml_meta": {"alias": "length_of_found_feature", "domain_of": ["PlannotateAnnotationReport"]}
        },
    )
    percent_match_length: Optional[float] = Field(
        None,
        json_schema_extra={
            "linkml_meta": {"alias": "percent_match_length", "domain_of": ["PlannotateAnnotationReport"]}
        },
    )
    fragment: Optional[bool] = Field(
        None, json_schema_extra={"linkml_meta": {"alias": "fragment", "domain_of": ["PlannotateAnnotationReport"]}}
    )
    database: Optional[str] = Field(
        None, json_schema_extra={"linkml_meta": {"alias": "database", "domain_of": ["PlannotateAnnotationReport"]}}
    )
    Feature: Optional[str] = Field(
        None, json_schema_extra={"linkml_meta": {"alias": "Feature", "domain_of": ["PlannotateAnnotationReport"]}}
    )
    Type: Optional[str] = Field(
        None, json_schema_extra={"linkml_meta": {"alias": "Type", "domain_of": ["PlannotateAnnotationReport"]}}
    )
    Description: Optional[str] = Field(
        None, json_schema_extra={"linkml_meta": {"alias": "Description", "domain_of": ["PlannotateAnnotationReport"]}}
    )
    sequence: Optional[str] = Field(
        None,
        json_schema_extra={
            "linkml_meta": {
                "alias": "sequence",
                "domain_of": ["Primer", "AssemblyFragment", "PlannotateAnnotationReport"],
            }
        },
    )
    type: Literal["PlannotateAnnotationReport"] = Field(
        "PlannotateAnnotationReport",
        description="""Designates the class""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "designates_type": True,
                "domain_of": ["Sequence", "Source", "AnnotationReport"],
            }
        },
    )


class AnnotationSource(Source):
    """
    Represents a computational step in which sequence features are annotated in a sequence
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {"from_schema": "https://w3id.org/genestorian/ShareYourCloning_LinkML"}
    )

    annotation_tool: AnnotationTool = Field(
        ..., json_schema_extra={"linkml_meta": {"alias": "annotation_tool", "domain_of": ["AnnotationSource"]}}
    )
    annotation_tool_version: Optional[str] = Field(
        None,
        description="""The version of the annotation tool""",
        json_schema_extra={"linkml_meta": {"alias": "annotation_tool_version", "domain_of": ["AnnotationSource"]}},
    )
    annotation_report: Optional[List[Union[AnnotationReport, PlannotateAnnotationReport]]] = Field(
        None, json_schema_extra={"linkml_meta": {"alias": "annotation_report", "domain_of": ["AnnotationSource"]}}
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
    type: Literal["AnnotationSource"] = Field(
        "AnnotationSource",
        description="""Designates the class""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "designates_type": True,
                "domain_of": ["Sequence", "Source", "AnnotationReport"],
            }
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
SnapGenePlasmidSource.model_rebuild()
EuroscarfSource.model_rebuild()
IGEMSource.model_rebuild()
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
InFusionSource.model_rebuild()
OverlapExtensionPCRLigationSource.model_rebuild()
RestrictionAndLigationSource.model_rebuild()
GatewaySource.model_rebuild()
CRISPRSource.model_rebuild()
OligoHybridizationSource.model_rebuild()
PolymeraseExtensionSource.model_rebuild()
CloningStrategy.model_rebuild()
AnnotationReport.model_rebuild()
PlannotateAnnotationReport.model_rebuild()
AnnotationSource.model_rebuild()
