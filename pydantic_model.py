from __future__ import annotations 
from datetime import (
    datetime,
    date
)
from decimal import Decimal 
from enum import Enum 
import re
import sys
from typing import (
    Any,
    List,
    Literal,
    Dict,
    Optional,
    Union
)
from pydantic.version import VERSION  as PYDANTIC_VERSION 
if int(PYDANTIC_VERSION[0])>=2:
    from pydantic import (
        BaseModel,
        ConfigDict,
        Field,
        field_validator
    )
else:
    from pydantic import (
        BaseModel,
        Field,
        validator
    )

metamodel_version = "None"
version = "None"


class WeakRefShimBaseModel(BaseModel):
    __slots__ = '__weakref__'

class ConfiguredBaseModel(WeakRefShimBaseModel,
                validate_assignment = True,
                validate_all = True,
                underscore_attrs_are_private = True,
                extra = "forbid",
                arbitrary_types_allowed = True,
                use_enum_values = True):
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
    overhang_crick_3prime: Optional[int] = Field(None, description="""Taken from pydna's `dseq::ovhg`An integer describing the length of the crick strand overhang in the 5' of the molecule, or 3' of the crick strand""")
    overhang_watson_3prime: Optional[int] = Field(None, description="""The equivalent of `overhang_crick_3prime` but for the watson strand""")
    id: int = Field(..., description="""A unique identifier for a thing""")
    type: Literal["TextFileSequence"] = Field("TextFileSequence", description="""The type of the source""")


class Primer(NamedThing):
    """
    An oligonucleotide or primer
    """
    id: int = Field(..., description="""A unique identifier for a thing""")
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""")
    sequence: Optional[str] = Field(None)

    @validator('sequence', allow_reuse=True)
    def pattern_sequence(cls, v):
        pattern=re.compile(r"^[acgtACGT]+$")
        if isinstance(v,list):
            for element in v:
                if not pattern.match(element):
                    raise ValueError(f"Invalid sequence format: {element}")
        elif isinstance(v,str):
            if not pattern.match(v):
                raise ValueError(f"Invalid sequence format: {v}")
        return v


class SequenceCut(ConfiguredBaseModel):
    """
    Represents a cut in a DNA sequence
    """
    cut_watson: Optional[int] = Field(None, description="""The position of the cut in the watson strand. The cut is made before the base at this position (zero-based), so that cut position 1 cuts after the first base.""")
    overhang: Optional[int] = Field(None, description="""The length of the overhang that is left after the cut. It can be negative, same meaning as in pydna's `dseq::ovhg` and biopython's `Bio.Restriction.RestrictionType.ovhg`.""")


class RestrictionSequenceCut(SequenceCut):
    """
    Represents a cut in a DNA sequence that is made by a restriction enzyme
    """
    restriction_enzyme: str = Field(...)
    cut_watson: Optional[int] = Field(None, description="""The position of the cut in the watson strand. The cut is made before the base at this position (zero-based), so that cut position 1 cuts after the first base.""")
    overhang: Optional[int] = Field(None, description="""The length of the overhang that is left after the cut. It can be negative, same meaning as in pydna's `dseq::ovhg` and biopython's `Bio.Restriction.RestrictionType.ovhg`.""")


class Source(NamedThing):
    """
    Represents the source of a sequence
    """
    input: Optional[List[int]] = Field(default_factory=list, description="""The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.""")
    output: Optional[int] = Field(None, description="""Identifier of the sequence that is the output of this source.""")
    type: Literal["Source"] = Field("Source", description="""The type of the source""")
    id: int = Field(..., description="""A unique identifier for a thing""")


class ManuallyTypedSource(Source):
    """
    Represents the source of a sequence that is manually typed by the user
    """
    user_input: str = Field(...)
    circular: Optional[bool] = Field(None, description="""Whether the sequence is circular or not""")
    input: Optional[List[int]] = Field(default_factory=list, description="""The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.""")
    output: Optional[int] = Field(None, description="""Identifier of the sequence that is the output of this source.""")
    type: Literal["ManuallyTypedSource"] = Field("ManuallyTypedSource", description="""The type of the source""")
    id: int = Field(..., description="""A unique identifier for a thing""")

    @validator('user_input', allow_reuse=True)
    def pattern_user_input(cls, v):
        pattern=re.compile(r"^[acgtACGT]+$")
        if isinstance(v,list):
            for element in v:
                if not pattern.match(element):
                    raise ValueError(f"Invalid user_input format: {element}")
        elif isinstance(v,str):
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
    input: Optional[List[int]] = Field(default_factory=list, description="""The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.""")
    output: Optional[int] = Field(None, description="""Identifier of the sequence that is the output of this source.""")
    type: Literal["UploadedFileSource"] = Field("UploadedFileSource", description="""The type of the source""")
    id: int = Field(..., description="""A unique identifier for a thing""")


class RepositoryIdSource(Source):
    """
    Represents the source of a sequence that is identified by a repository id
    """
    repository_name: RepositoryName = Field(...)
    repository_id: str = Field(..., description="""The id of the sequence in the repository""")
    input: Optional[List[int]] = Field(default_factory=list, description="""The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.""")
    output: Optional[int] = Field(None, description="""Identifier of the sequence that is the output of this source.""")
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
    start: int = Field(..., description="""The starting coordinate (1-based) of the sequence in the sequence accession""")
    stop: int = Field(..., description="""The ending coordinate (1-based) of the sequence in the sequence accession""")
    strand: int = Field(..., description="""The strand of the sequence in the sequence accession, should be 1 or -1""")
    input: Optional[List[int]] = Field(default_factory=list, description="""The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.""")
    output: Optional[int] = Field(None, description="""Identifier of the sequence that is the output of this source.""")
    type: Literal["GenomeCoordinatesSource"] = Field("GenomeCoordinatesSource", description="""The type of the source""")
    id: int = Field(..., description="""A unique identifier for a thing""")


class CutSource(Source):
    """
    Represents the source of a sequence that is a subfragment of another sequence, generated by sequence cutting.
    """
    left_edge: Optional[SequenceCut] = Field(None)
    right_edge: Optional[SequenceCut] = Field(None)
    input: Optional[List[int]] = Field(default_factory=list, description="""The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.""")
    output: Optional[int] = Field(None, description="""Identifier of the sequence that is the output of this source.""")
    type: Literal["CutSource"] = Field("CutSource", description="""The type of the source""")
    id: int = Field(..., description="""A unique identifier for a thing""")


class RestrictionCutSource(CutSource):
    """
    Represents the source of a sequence that is a subfragment of another sequence, generated by sequence cutting using restriction enzymes.
    """
    left_edge: Optional[RestrictionSequenceCut] = Field(None)
    right_edge: Optional[RestrictionSequenceCut] = Field(None)
    input: Optional[List[int]] = Field(default_factory=list, description="""The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.""")
    output: Optional[int] = Field(None, description="""Identifier of the sequence that is the output of this source.""")
    type: Literal["RestrictionCutSource"] = Field("RestrictionCutSource", description="""The type of the source""")
    id: int = Field(..., description="""A unique identifier for a thing""")


class CloningStrategy(ConfiguredBaseModel):
    """
    Represents a cloning strategy
    """
    sequences: List[Union[Sequence,TextFileSequence]] = Field(default_factory=list, description="""The sequences that are used in the cloning strategy""")
    sources: List[Union[Source,ManuallyTypedSource,UploadedFileSource,RepositoryIdSource,GenomeCoordinatesSource,CutSource,RestrictionCutSource]] = Field(default_factory=list, description="""The sources of the sequences that are used in the cloning strategy""")
    primers: Optional[List[int]] = Field(default_factory=list, description="""The primers that are used in the cloning strategy""")
    description: Optional[str] = Field(None, description="""A description of the cloning strategy""")


# Update forward refs
# see https://pydantic-docs.helpmanual.io/usage/postponed_annotations/
NamedThing.update_forward_refs()
Sequence.update_forward_refs()
TextFileSequence.update_forward_refs()
Primer.update_forward_refs()
SequenceCut.update_forward_refs()
RestrictionSequenceCut.update_forward_refs()
Source.update_forward_refs()
ManuallyTypedSource.update_forward_refs()
UploadedFileSource.update_forward_refs()
RepositoryIdSource.update_forward_refs()
GenomeCoordinatesSource.update_forward_refs()
CutSource.update_forward_refs()
RestrictionCutSource.update_forward_refs()
CloningStrategy.update_forward_refs()

