from __future__ import annotations
from datetime import datetime, date
from enum import Enum

from decimal import Decimal
from typing import List, Dict, Optional, Any, Union
from pydantic import BaseModel as BaseModel, Field, validator
import re
import sys
if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


metamodel_version = "None"
version = "None"

class WeakRefShimBaseModel(BaseModel):
   __slots__ = '__weakref__'

class ConfiguredBaseModel(WeakRefShimBaseModel,
                validate_assignment = True,
                validate_all = True,
                underscore_attrs_are_private = True,
                extra = 'forbid',
                arbitrary_types_allowed = True,
                use_enum_values = True):

    pass

        

class RepositoryName(str, Enum):
    
    # Addgene
    addgene = "addgene"
    # GenBank
    genbank = "genbank"
    
    

class SourceType(str, Enum):
    
    
    repository_id = "repository_id"
    
    file = "file"
    
    restriction = "restriction"
    
    ligation = "ligation"
    
    PCR = "PCR"
    
    homologous_recombination = "homologous_recombination"
    
    gibson_assembly = "gibson_assembly"
    
    restriction_and_ligation = "restriction_and_ligation"
    
    genome_coordinates = "genome_coordinates"
    
    manually_typed = "manually_typed"
    
    

class NamedThing(ConfiguredBaseModel):
    
    id: int = Field(..., description="""A unique identifier for a thing""")
    
    

class Source(NamedThing):
    """
    Represents the source of a sequence
    """
    input: List[int] = Field(default_factory=list, description="""Identifiers of the sequences that are an input to this source. If the source represents external import of a sequence, it's empty.""")
    output: int = Field(..., description="""Identifier of the sequence that is the output of this source.""")
    type: SourceType = Field(..., description="""The type of the source""")
    kind: str = Field(..., description="""The kind entity (always equal to \"source\"). Should probably be removed.""")
    id: int = Field(..., description="""A unique identifier for a thing""")
    
    

class ManuallyTypedSource(Source):
    """
    Represents the source of a sequence that is manually typed by the user
    """
    user_input: Optional[str] = Field(None)
    input: List[int] = Field(default_factory=list, description="""Identifiers of the sequences that are an input to this source. If the source represents external import of a sequence, it's empty.""")
    output: int = Field(..., description="""Identifier of the sequence that is the output of this source.""")
    type: SourceType = Field(..., description="""The type of the source""")
    kind: str = Field(..., description="""The kind entity (always equal to \"source\"). Should probably be removed.""")
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
    file_name: Optional[str] = Field(None, description="""The name of the file""")
    index_in_file: Optional[int] = Field(None, description="""The index of the sequence in the file""")
    input: List[int] = Field(default_factory=list, description="""Identifiers of the sequences that are an input to this source. If the source represents external import of a sequence, it's empty.""")
    output: int = Field(..., description="""Identifier of the sequence that is the output of this source.""")
    type: SourceType = Field(..., description="""The type of the source""")
    kind: str = Field(..., description="""The kind entity (always equal to \"source\"). Should probably be removed.""")
    id: int = Field(..., description="""A unique identifier for a thing""")
    
    

class RepositoryIdSource(Source):
    """
    Represents the source of a sequence that is identified by a repository id
    """
    repository_name: RepositoryName = Field(...)
    repository_id: str = Field(..., description="""The id of the sequence in the repository""")
    input: List[int] = Field(default_factory=list, description="""Identifiers of the sequences that are an input to this source. If the source represents external import of a sequence, it's empty.""")
    output: int = Field(..., description="""Identifier of the sequence that is the output of this source.""")
    type: SourceType = Field(..., description="""The type of the source""")
    kind: str = Field(..., description="""The kind entity (always equal to \"source\"). Should probably be removed.""")
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
    input: List[int] = Field(default_factory=list, description="""Identifiers of the sequences that are an input to this source. If the source represents external import of a sequence, it's empty.""")
    output: int = Field(..., description="""Identifier of the sequence that is the output of this source.""")
    type: SourceType = Field(..., description="""The type of the source""")
    kind: str = Field(..., description="""The kind entity (always equal to \"source\"). Should probably be removed.""")
    id: int = Field(..., description="""A unique identifier for a thing""")
    
    


# Update forward refs
# see https://pydantic-docs.helpmanual.io/usage/postponed_annotations/
NamedThing.update_forward_refs()
Source.update_forward_refs()
ManuallyTypedSource.update_forward_refs()
UploadedFileSource.update_forward_refs()
RepositoryIdSource.update_forward_refs()
GenomeCoordinatesSource.update_forward_refs()

