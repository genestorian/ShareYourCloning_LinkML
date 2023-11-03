from __future__ import annotations
from datetime import datetime, date
from enum import Enum
from typing import List, Dict, Optional, Any, Union
from pydantic import BaseModel as BaseModel, Field
from linkml_runtime.linkml_model import Decimal
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
    
    
    addgene = "addgene"
    
    genbank = "genbank"
    
    

class NamedThing(ConfiguredBaseModel):
    """
    A generic grouping for any identifiable entity
    """
    id: Optional[int] = Field(None, description="""A unique identifier for a thing""")
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""")
    description: Optional[str] = Field(None, description="""A human-readable description for a thing""")
    


class CloningStrategy(NamedThing):
    """
    Represents a cloning strategy
    """
    description: Optional[str] = Field(None, description="""A human-readable description for a thing""")
    sequences: Optional[List[int]] = Field(default_factory=list)
    sources: Optional[List[int]] = Field(default_factory=list)
    id: int = Field(..., description="""A unique identifier for a thing""")
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""")
    


class Source(NamedThing):
    """
    Represents the source of a sequence
    """
    id: int = Field(..., description="""A unique identifier for a thing""")
    has_input: Optional[Dict[int, Sequence]] = Field(None)
    has_output: Optional[Sequence] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""")
    description: Optional[str] = Field(None, description="""A human-readable description for a thing""")
    


class RepositoryIdSource(Source):
    """
    Represents the source of a sequence that is identified by a repository id
    """
    repository_id: str = Field(...)
    id: int = Field(..., description="""A unique identifier for a thing""")
    has_input: Optional[Dict[int, Sequence]] = Field(None)
    has_output: Optional[Sequence] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""")
    description: Optional[str] = Field(None, description="""A human-readable description for a thing""")
    


class Sequence(NamedThing):
    """
    Represents a sequence
    """
    id: int = Field(..., description="""A unique identifier for a thing""")
    file_extension: Optional[str] = Field(None)
    file_content: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""")
    description: Optional[str] = Field(None, description="""A human-readable description for a thing""")
    



# Update forward refs
# see https://pydantic-docs.helpmanual.io/usage/postponed_annotations/
NamedThing.update_forward_refs()
CloningStrategy.update_forward_refs()
Source.update_forward_refs()
RepositoryIdSource.update_forward_refs()
Sequence.update_forward_refs()

