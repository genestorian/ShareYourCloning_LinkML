from __future__ import annotations
from datetime import datetime, date
from decimal import Decimal
from enum import Enum
import re
import sys
from typing import Any, List, Literal, Dict, Optional, Union
from pydantic.version import VERSION as PYDANTIC_VERSION

if int(PYDANTIC_VERSION[0]) >= 2:
    from pydantic import BaseModel, ConfigDict, Field, field_validator
else:
    from pydantic import BaseModel, Field, validator

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


class RepositoryName(str, Enum):
    # Addgene
    addgene = "addgene"
    # GenBank
    genbank = "genbank"


class SequenceFileFormat(str, Enum):
    fasta = "fasta"
    genbank = "genbank"
    snapgene = "snapgene"


class NamedThing(ConfiguredBaseModel):
    id: int = Field(..., description="""A unique identifier for a thing""")


class Sequence(NamedThing):
    """
    Represents a sequence
    """

    id: int = Field(..., description="""A unique identifier for a thing""")
    type: Literal["Sequence"] = Field("Sequence", description="""The type of the source""")


class TextFileSequence(Sequence):
    """
    A sequence (may have features) defined by the content of a text file
    """

    sequence_file_format: SequenceFileFormat = Field(..., description="""The format of a sequence file""")
    file_content: Optional[str] = Field(None)
    overhang_crick_3prime: Optional[int] = Field(
        None,
        description="""Taken from pydna's `dseq::ovhg`An integer describing the length of the crick strand overhang in the 5' of the molecule, or 3' of the crick strand""",
    )
    overhang_watson_3prime: Optional[int] = Field(
        None,
        description="""The equivalent of `overhang_crick_3prime` but for the watson strand""",
    )
    id: int = Field(..., description="""A unique identifier for a thing""")
    type: Literal["TextFileSequence"] = Field("TextFileSequence", description="""The type of the source""")


class Primer(Sequence):
    """
    An oligonucleotide or primer
    """

    name: Optional[str] = Field(None, description="""A human-readable name for a thing""")
    sequence: Optional[str] = Field(None)
    id: int = Field(..., description="""A unique identifier for a thing""")
    type: Literal["Primer"] = Field("Primer", description="""The type of the source""")

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

    cut_watson: Optional[int] = Field(
        None,
        description="""The position of the cut in the watson strand. The cut is made before the base at this position (zero-based), so that cut position 1 cuts after the first base.""",
    )
    overhang: Optional[int] = Field(
        None,
        description="""The length of the overhang that is left after the cut. It can be negative, same meaning as in pydna's `dseq::ovhg` and biopython's `Bio.Restriction.RestrictionType.ovhg`.""",
    )


class RestrictionSequenceCut(SequenceCut):
    """
    Represents a cut in a DNA sequence that is made by a restriction enzyme
    """

    restriction_enzyme: str = Field(...)
    cut_watson: Optional[int] = Field(
        None,
        description="""The position of the cut in the watson strand. The cut is made before the base at this position (zero-based), so that cut position 1 cuts after the first base.""",
    )
    overhang: Optional[int] = Field(
        None,
        description="""The length of the overhang that is left after the cut. It can be negative, same meaning as in pydna's `dseq::ovhg` and biopython's `Bio.Restriction.RestrictionType.ovhg`.""",
    )


class Source(NamedThing):
    """
    Represents the source of a sequence
    """

    input: Optional[List[int]] = Field(
        default_factory=list,
        description="""The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.""",
    )
    output: Optional[int] = Field(
        None,
        description="""Identifier of the sequence that is the output of this source.""",
    )
    type: Literal["Source"] = Field("Source", description="""The type of the source""")
    id: int = Field(..., description="""A unique identifier for a thing""")


class ManuallyTypedSource(Source):
    """
    Represents the source of a sequence that is manually typed by the user
    """

    user_input: str = Field(...)
    circular: Optional[bool] = Field(None, description="""Whether the sequence is circular or not""")
    input: Optional[List[int]] = Field(
        default_factory=list,
        description="""The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.""",
    )
    output: Optional[int] = Field(
        None,
        description="""Identifier of the sequence that is the output of this source.""",
    )
    type: Literal["ManuallyTypedSource"] = Field("ManuallyTypedSource", description="""The type of the source""")
    id: int = Field(..., description="""A unique identifier for a thing""")

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

    sequence_file_format: SequenceFileFormat = Field(..., description="""The format of a sequence file""")
    file_name: Optional[str] = Field(None, description="""The name of the file""")
    index_in_file: Optional[int] = Field(None, description="""The index of the sequence in the file""")
    input: Optional[List[int]] = Field(
        default_factory=list,
        description="""The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.""",
    )
    output: Optional[int] = Field(
        None,
        description="""Identifier of the sequence that is the output of this source.""",
    )
    type: Literal["UploadedFileSource"] = Field("UploadedFileSource", description="""The type of the source""")
    id: int = Field(..., description="""A unique identifier for a thing""")


class RepositoryIdSource(Source):
    """
    Represents the source of a sequence that is identified by a repository id
    """

    repository_name: RepositoryName = Field(...)
    repository_id: str = Field(..., description="""The id of the sequence in the repository""")
    input: Optional[List[int]] = Field(
        default_factory=list,
        description="""The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.""",
    )
    output: Optional[int] = Field(
        None,
        description="""Identifier of the sequence that is the output of this source.""",
    )
    type: Literal["RepositoryIdSource"] = Field("RepositoryIdSource", description="""The type of the source""")
    id: int = Field(..., description="""A unique identifier for a thing""")


class GenomeCoordinatesSource(Source):
    """
    Represents the source of a sequence that is identified by genome coordinates, requested from NCBI
    """

    assembly_accession: Optional[str] = Field(None, description="""The accession of the assembly""")
    sequence_accession: str = Field(..., description="""The accession of the sequence""")
    locus_tag: Optional[str] = Field(None, description="""The locus tag of the sequence""")
    gene_id: Optional[int] = Field(None, description="""The gene id of the sequence""")
    start: int = Field(
        ...,
        description="""The starting coordinate (1-based) of the sequence in the sequence accession""",
    )
    end: int = Field(
        ...,
        description="""The ending coordinate (1-based) of the sequence in the sequence accession""",
    )
    strand: int = Field(
        ...,
        description="""The strand of the sequence in the sequence accession, should be 1 or -1""",
    )
    input: Optional[List[int]] = Field(
        default_factory=list,
        description="""The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.""",
    )
    output: Optional[int] = Field(
        None,
        description="""Identifier of the sequence that is the output of this source.""",
    )
    type: Literal["GenomeCoordinatesSource"] = Field(
        "GenomeCoordinatesSource", description="""The type of the source"""
    )
    id: int = Field(..., description="""A unique identifier for a thing""")


class SequenceCutSource(Source):
    """
    Represents the source of a sequence that is a subfragment of another sequence, generated by sequence cutting.
    """

    left_edge: Optional[SequenceCut] = Field(None)
    right_edge: Optional[SequenceCut] = Field(None)
    input: Optional[List[int]] = Field(
        default_factory=list,
        description="""The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.""",
    )
    output: Optional[int] = Field(
        None,
        description="""Identifier of the sequence that is the output of this source.""",
    )
    type: Literal["SequenceCutSource"] = Field("SequenceCutSource", description="""The type of the source""")
    id: int = Field(..., description="""A unique identifier for a thing""")


class RestrictionEnzymeDigestionSource(SequenceCutSource):
    """
    Represents the source of a sequence that is a subfragment of another sequence, generated by sequence cutting using restriction enzymes.
    """

    left_edge: Optional[RestrictionSequenceCut] = Field(None)
    right_edge: Optional[RestrictionSequenceCut] = Field(None)
    input: Optional[List[int]] = Field(
        default_factory=list,
        description="""The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.""",
    )
    output: Optional[int] = Field(
        None,
        description="""Identifier of the sequence that is the output of this source.""",
    )
    type: Literal["RestrictionEnzymeDigestionSource"] = Field(
        "RestrictionEnzymeDigestionSource", description="""The type of the source"""
    )
    id: int = Field(..., description="""A unique identifier for a thing""")


class SimpleSequenceLocation(ConfiguredBaseModel):
    """
    Represents a location within a sequence, for now support for ranges only
    """

    start: int = Field(..., description="""The starting coordinate (1-based) of the location""")
    end: int = Field(..., description="""The ending coordinate (1-based) of the location""")
    strand: Optional[int] = Field(None, description="""The strand of the location, should be 1 or -1 or null""")


class AssemblyJoin(ConfiguredBaseModel):
    """
    Represents a joint between two fragments in an assembly
    """

    left_fragment: int = Field(...)
    right_fragment: int = Field(...)
    left_location: SimpleSequenceLocation = Field(
        ...,
        description="""Location of the overlap in the left fragment. Might be an empty location (start == end) to indicate blunt join.""",
    )
    right_location: SimpleSequenceLocation = Field(
        ...,
        description="""Location of the overlap in the right fragment. Might be an empty location (start == end) to indicate blunt join.""",
    )


class AssemblySource(Source):
    """
    Represents the source of a sequence that is an assembly of other sequences
    """

    circular: Optional[bool] = Field(None, description="""Whether the assembly is circular or not""")
    assembly: List[AssemblyJoin] = Field(
        default_factory=list,
        description="""The joins between the fragments in the assembly""",
    )
    input: Optional[List[int]] = Field(
        default_factory=list,
        description="""The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.""",
    )
    output: Optional[int] = Field(
        None,
        description="""Identifier of the sequence that is the output of this source.""",
    )
    type: Literal["AssemblySource"] = Field("AssemblySource", description="""The type of the source""")
    id: int = Field(..., description="""A unique identifier for a thing""")


class PCRSource(AssemblySource):
    """
    Represents the source of a sequence that is generated by PCR
    """

    forward_primer: int = Field(..., description="""The forward primer used in the PCR""")
    reverse_primer: int = Field(..., description="""The reverse primer used in the PCR""")
    circular: Optional[bool] = Field(None, description="""Whether the assembly is circular or not""")
    assembly: List[AssemblyJoin] = Field(
        default_factory=list,
        description="""The joins between the fragments in the assembly""",
    )
    input: Optional[List[int]] = Field(
        default_factory=list,
        description="""The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.""",
    )
    output: Optional[int] = Field(
        None,
        description="""Identifier of the sequence that is the output of this source.""",
    )
    type: Literal["PCRSource"] = Field("PCRSource", description="""The type of the source""")
    id: int = Field(..., description="""A unique identifier for a thing""")


class LigationSource(AssemblySource):
    """
    Represents the source of a sequence that is generated by ligation with sticky or blunt ends.
    """

    circular: Optional[bool] = Field(None, description="""Whether the assembly is circular or not""")
    assembly: List[AssemblyJoin] = Field(
        default_factory=list,
        description="""The joins between the fragments in the assembly""",
    )
    input: Optional[List[int]] = Field(
        default_factory=list,
        description="""The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.""",
    )
    output: Optional[int] = Field(
        None,
        description="""Identifier of the sequence that is the output of this source.""",
    )
    type: Literal["LigationSource"] = Field("LigationSource", description="""The type of the source""")
    id: int = Field(..., description="""A unique identifier for a thing""")


class HomologousRecombinationSource(AssemblySource):
    """
    Represents the source of a sequence that is generated by homologous recombination
    """

    circular: Optional[bool] = Field(None, description="""Whether the assembly is circular or not""")
    assembly: List[AssemblyJoin] = Field(
        default_factory=list,
        description="""The joins between the fragments in the assembly""",
    )
    input: Optional[List[int]] = Field(
        default_factory=list,
        description="""The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.""",
    )
    output: Optional[int] = Field(
        None,
        description="""Identifier of the sequence that is the output of this source.""",
    )
    type: Literal["HomologousRecombinationSource"] = Field(
        "HomologousRecombinationSource", description="""The type of the source"""
    )
    id: int = Field(..., description="""A unique identifier for a thing""")


class GibsonAssemblySource(AssemblySource):
    """
    Represents the source of a sequence that is generated by Gibson assembly
    """

    circular: Optional[bool] = Field(None, description="""Whether the assembly is circular or not""")
    assembly: List[AssemblyJoin] = Field(
        default_factory=list,
        description="""The joins between the fragments in the assembly""",
    )
    input: Optional[List[int]] = Field(
        default_factory=list,
        description="""The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.""",
    )
    output: Optional[int] = Field(
        None,
        description="""Identifier of the sequence that is the output of this source.""",
    )
    type: Literal["GibsonAssemblySource"] = Field("GibsonAssemblySource", description="""The type of the source""")
    id: int = Field(..., description="""A unique identifier for a thing""")


class RestrictionAndLigationSource(AssemblySource):
    """
    Represents the source of a sequence that is generated by restriction and ligation
    """

    restriction_enzymes: List[str] = Field(default_factory=list)
    circular: Optional[bool] = Field(None, description="""Whether the assembly is circular or not""")
    assembly: List[AssemblyJoin] = Field(
        default_factory=list,
        description="""The joins between the fragments in the assembly""",
    )
    input: Optional[List[int]] = Field(
        default_factory=list,
        description="""The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.""",
    )
    output: Optional[int] = Field(
        None,
        description="""Identifier of the sequence that is the output of this source.""",
    )
    type: Literal["RestrictionAndLigationSource"] = Field(
        "RestrictionAndLigationSource", description="""The type of the source"""
    )
    id: int = Field(..., description="""A unique identifier for a thing""")


class OligoHybridizationSource(Source):
    """
    Represents the source of a sequence that is generated by oligo hybridization
    """

    forward_oligo: int = Field(..., description="""The forward oligo used in the hybridization""")
    reverse_oligo: int = Field(..., description="""The reverse oligo used in the hybridization""")
    overhang_crick_3prime: Optional[int] = Field(
        None,
        description="""The length of the crick strand overhang in the 5' of the molecule, or 3' of the crick strand.""",
    )
    input: Optional[List[int]] = Field(
        default_factory=list,
        description="""The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.""",
    )
    output: Optional[int] = Field(
        None,
        description="""Identifier of the sequence that is the output of this source.""",
    )
    type: Literal["OligoHybridizationSource"] = Field(
        "OligoHybridizationSource", description="""The type of the source"""
    )
    id: int = Field(..., description="""A unique identifier for a thing""")


class PolymeraseExtensionSource(Source):
    """
    Represents the source of a sequence that is generated by polymerase extension
    """

    input: Optional[List[int]] = Field(
        default_factory=list,
        description="""The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.""",
    )
    output: Optional[int] = Field(
        None,
        description="""Identifier of the sequence that is the output of this source.""",
    )
    type: Literal["PolymeraseExtensionSource"] = Field(
        "PolymeraseExtensionSource", description="""The type of the source"""
    )
    id: int = Field(..., description="""A unique identifier for a thing""")


class CloningStrategy(ConfiguredBaseModel):
    """
    Represents a cloning strategy
    """

    sequences: List[Union[Sequence, TextFileSequence, Primer]] = Field(
        default_factory=list,
        description="""The sequences that are used in the cloning strategy""",
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
            RestrictionAndLigationSource,
            RestrictionEnzymeDigestionSource,
        ]
    ] = Field(
        default_factory=list,
        description="""The sources of the sequences that are used in the cloning strategy""",
    )
    primers: Optional[List[int]] = Field(
        default_factory=list,
        description="""The primers that are used in the cloning strategy""",
    )
    description: Optional[str] = Field(None, description="""A description of the cloning strategy""")


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
GenomeCoordinatesSource.model_rebuild()
SequenceCutSource.model_rebuild()
RestrictionEnzymeDigestionSource.model_rebuild()
SimpleSequenceLocation.model_rebuild()
AssemblyJoin.model_rebuild()
AssemblySource.model_rebuild()
PCRSource.model_rebuild()
LigationSource.model_rebuild()
HomologousRecombinationSource.model_rebuild()
GibsonAssemblySource.model_rebuild()
RestrictionAndLigationSource.model_rebuild()
OligoHybridizationSource.model_rebuild()
PolymeraseExtensionSource.model_rebuild()
CloningStrategy.model_rebuild()
