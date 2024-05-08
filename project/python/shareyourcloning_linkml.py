# Auto generated from shareyourcloning_linkml.yaml by pythongen.py version: 0.0.1
# Generation date: 2024-05-08T17:38:07
# Schema: ShareYourCloning_LinkML
#
# id: https://w3id.org/genestorian/ShareYourCloning_LinkML
# description: A LinkML data model for ShareYourCloning
# license: MIT

import dataclasses
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from datetime import date, datetime
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import Boolean, Integer, String
from linkml_runtime.utils.metamodelcore import Bool

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
OBI = CurieNamespace("OBI", "http://purl.obolibrary.org/obo/OBI_")
PATO = CurieNamespace("PATO", "http://purl.obolibrary.org/obo/PATO_")
BIOLINK = CurieNamespace("biolink", "https://w3id.org/biolink/")
EXAMPLE = CurieNamespace("example", "https://example.org/")
LINKML = CurieNamespace("linkml", "https://w3id.org/linkml/")
SCHEMA = CurieNamespace("schema", "http://schema.org/")
SHAREYOURCLONING_LINKML = CurieNamespace(
    "shareyourcloning_linkml", "https://w3id.org/genestorian/ShareYourCloning_LinkML/"
)
DEFAULT_ = SHAREYOURCLONING_LINKML


# Types


# Class references
class NamedThingId(extended_int):
    pass


class SequenceId(NamedThingId):
    pass


class TextFileSequenceId(SequenceId):
    pass


class PrimerId(SequenceId):
    pass


class SourceId(NamedThingId):
    pass


class ManuallyTypedSourceId(SourceId):
    pass


class UploadedFileSourceId(SourceId):
    pass


class RepositoryIdSourceId(SourceId):
    pass


class AddGeneIdSourceId(RepositoryIdSourceId):
    pass


class GenomeCoordinatesSourceId(SourceId):
    pass


class SequenceCutSourceId(SourceId):
    pass


class RestrictionEnzymeDigestionSourceId(SequenceCutSourceId):
    pass


class AssemblySourceId(SourceId):
    pass


class PCRSourceId(AssemblySourceId):
    pass


class LigationSourceId(AssemblySourceId):
    pass


class HomologousRecombinationSourceId(AssemblySourceId):
    pass


class GibsonAssemblySourceId(AssemblySourceId):
    pass


class RestrictionAndLigationSourceId(AssemblySourceId):
    pass


class CRISPRSourceId(HomologousRecombinationSourceId):
    pass


class OligoHybridizationSourceId(SourceId):
    pass


class PolymeraseExtensionSourceId(SourceId):
    pass


@dataclass
class NamedThing(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["Thing"]
    class_class_curie: ClassVar[str] = "schema:Thing"
    class_name: ClassVar[str] = "NamedThing"
    class_model_uri: ClassVar[URIRef] = SHAREYOURCLONING_LINKML.NamedThing

    id: Union[int, NamedThingId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NamedThingId):
            self.id = NamedThingId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Sequence(NamedThing):
    """
    Represents a sequence
    """

    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SHAREYOURCLONING_LINKML["Sequence"]
    class_class_curie: ClassVar[str] = "shareyourcloning_linkml:Sequence"
    class_name: ClassVar[str] = "Sequence"
    class_model_uri: ClassVar[URIRef] = SHAREYOURCLONING_LINKML.Sequence

    id: Union[int, SequenceId] = None
    type: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SequenceId):
            self.id = SequenceId(self.id)

        self.type = str(self.class_name)

        super().__post_init__(**kwargs)

    def __new__(cls, *args, **kwargs):

        type_designator = "type"
        if not type_designator in kwargs:
            return super().__new__(cls, *args, **kwargs)
        else:
            type_designator_value = kwargs[type_designator]
            target_cls = cls._class_for("class_name", type_designator_value)

            if target_cls is None:
                raise ValueError(
                    f"Wrong type designator value: class {cls.__name__} "
                    f"has no subclass with ['class_name']='{kwargs[type_designator]}'"
                )
            return super().__new__(target_cls, *args, **kwargs)


@dataclass
class TextFileSequence(Sequence):
    """
    A sequence (may have features) defined by the content of a text file
    """

    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SHAREYOURCLONING_LINKML["TextFileSequence"]
    class_class_curie: ClassVar[str] = "shareyourcloning_linkml:TextFileSequence"
    class_name: ClassVar[str] = "TextFileSequence"
    class_model_uri: ClassVar[URIRef] = SHAREYOURCLONING_LINKML.TextFileSequence

    id: Union[int, TextFileSequenceId] = None
    sequence_file_format: Union[str, "SequenceFileFormat"] = None
    overhang_crick_3prime: Optional[int] = 0
    overhang_watson_3prime: Optional[int] = 0
    file_content: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TextFileSequenceId):
            self.id = TextFileSequenceId(self.id)

        if self._is_empty(self.sequence_file_format):
            self.MissingRequiredField("sequence_file_format")
        if not isinstance(self.sequence_file_format, SequenceFileFormat):
            self.sequence_file_format = SequenceFileFormat(self.sequence_file_format)

        if self.overhang_crick_3prime is not None and not isinstance(self.overhang_crick_3prime, int):
            self.overhang_crick_3prime = int(self.overhang_crick_3prime)

        if self.overhang_watson_3prime is not None and not isinstance(self.overhang_watson_3prime, int):
            self.overhang_watson_3prime = int(self.overhang_watson_3prime)

        if self.file_content is not None and not isinstance(self.file_content, str):
            self.file_content = str(self.file_content)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class Primer(Sequence):
    """
    An oligonucleotide or primer
    """

    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SHAREYOURCLONING_LINKML["Primer"]
    class_class_curie: ClassVar[str] = "shareyourcloning_linkml:Primer"
    class_name: ClassVar[str] = "Primer"
    class_model_uri: ClassVar[URIRef] = SHAREYOURCLONING_LINKML.Primer

    id: Union[int, PrimerId] = None
    name: Optional[str] = None
    sequence: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PrimerId):
            self.id = PrimerId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.sequence is not None and not isinstance(self.sequence, str):
            self.sequence = str(self.sequence)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class SequenceCut(YAMLRoot):
    """
    Represents a cut in a DNA sequence
    """

    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SHAREYOURCLONING_LINKML["SequenceCut"]
    class_class_curie: ClassVar[str] = "shareyourcloning_linkml:SequenceCut"
    class_name: ClassVar[str] = "SequenceCut"
    class_model_uri: ClassVar[URIRef] = SHAREYOURCLONING_LINKML.SequenceCut

    cut_watson: int = None
    overhang: int = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.cut_watson):
            self.MissingRequiredField("cut_watson")
        if not isinstance(self.cut_watson, int):
            self.cut_watson = int(self.cut_watson)

        if self._is_empty(self.overhang):
            self.MissingRequiredField("overhang")
        if not isinstance(self.overhang, int):
            self.overhang = int(self.overhang)

        super().__post_init__(**kwargs)


@dataclass
class RestrictionSequenceCut(SequenceCut):
    """
    Represents a cut in a DNA sequence that is made by a restriction enzyme
    """

    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SHAREYOURCLONING_LINKML["RestrictionSequenceCut"]
    class_class_curie: ClassVar[str] = "shareyourcloning_linkml:RestrictionSequenceCut"
    class_name: ClassVar[str] = "RestrictionSequenceCut"
    class_model_uri: ClassVar[URIRef] = SHAREYOURCLONING_LINKML.RestrictionSequenceCut

    cut_watson: int = None
    overhang: int = None
    restriction_enzyme: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.restriction_enzyme):
            self.MissingRequiredField("restriction_enzyme")
        if not isinstance(self.restriction_enzyme, str):
            self.restriction_enzyme = str(self.restriction_enzyme)

        super().__post_init__(**kwargs)


@dataclass
class Source(NamedThing):
    """
    Represents the source of a sequence
    """

    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SHAREYOURCLONING_LINKML["Source"]
    class_class_curie: ClassVar[str] = "shareyourcloning_linkml:Source"
    class_name: ClassVar[str] = "Source"
    class_model_uri: ClassVar[URIRef] = SHAREYOURCLONING_LINKML.Source

    id: Union[int, SourceId] = None
    input: Optional[Union[Union[int, SequenceId], List[Union[int, SequenceId]]]] = empty_list()
    output: Optional[Union[int, SequenceId]] = None
    type: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.input, list):
            self.input = [self.input] if self.input is not None else []
        self.input = [v if isinstance(v, SequenceId) else SequenceId(v) for v in self.input]

        if self.output is not None and not isinstance(self.output, SequenceId):
            self.output = SequenceId(self.output)

        self.type = str(self.class_name)

        super().__post_init__(**kwargs)

    def __new__(cls, *args, **kwargs):

        type_designator = "type"
        if not type_designator in kwargs:
            return super().__new__(cls, *args, **kwargs)
        else:
            type_designator_value = kwargs[type_designator]
            target_cls = cls._class_for("class_name", type_designator_value)

            if target_cls is None:
                raise ValueError(
                    f"Wrong type designator value: class {cls.__name__} "
                    f"has no subclass with ['class_name']='{kwargs[type_designator]}'"
                )
            return super().__new__(target_cls, *args, **kwargs)


@dataclass
class ManuallyTypedSource(Source):
    """
    Represents the source of a sequence that is manually typed by the user
    """

    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SHAREYOURCLONING_LINKML["ManuallyTypedSource"]
    class_class_curie: ClassVar[str] = "shareyourcloning_linkml:ManuallyTypedSource"
    class_name: ClassVar[str] = "ManuallyTypedSource"
    class_model_uri: ClassVar[URIRef] = SHAREYOURCLONING_LINKML.ManuallyTypedSource

    id: Union[int, ManuallyTypedSourceId] = None
    user_input: str = None
    overhang_crick_3prime: Optional[int] = 0
    overhang_watson_3prime: Optional[int] = 0
    circular: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ManuallyTypedSourceId):
            self.id = ManuallyTypedSourceId(self.id)

        if self._is_empty(self.user_input):
            self.MissingRequiredField("user_input")
        if not isinstance(self.user_input, str):
            self.user_input = str(self.user_input)

        if self.overhang_crick_3prime is not None and not isinstance(self.overhang_crick_3prime, int):
            self.overhang_crick_3prime = int(self.overhang_crick_3prime)

        if self.overhang_watson_3prime is not None and not isinstance(self.overhang_watson_3prime, int):
            self.overhang_watson_3prime = int(self.overhang_watson_3prime)

        if self.circular is not None and not isinstance(self.circular, Bool):
            self.circular = Bool(self.circular)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class UploadedFileSource(Source):
    """
    Represents the source of a sequence that is uploaded as a file
    """

    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SHAREYOURCLONING_LINKML["UploadedFileSource"]
    class_class_curie: ClassVar[str] = "shareyourcloning_linkml:UploadedFileSource"
    class_name: ClassVar[str] = "UploadedFileSource"
    class_model_uri: ClassVar[URIRef] = SHAREYOURCLONING_LINKML.UploadedFileSource

    id: Union[int, UploadedFileSourceId] = None
    sequence_file_format: Union[str, "SequenceFileFormat"] = None
    file_name: Optional[str] = None
    index_in_file: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, UploadedFileSourceId):
            self.id = UploadedFileSourceId(self.id)

        if self._is_empty(self.sequence_file_format):
            self.MissingRequiredField("sequence_file_format")
        if not isinstance(self.sequence_file_format, SequenceFileFormat):
            self.sequence_file_format = SequenceFileFormat(self.sequence_file_format)

        if self.file_name is not None and not isinstance(self.file_name, str):
            self.file_name = str(self.file_name)

        if self.index_in_file is not None and not isinstance(self.index_in_file, int):
            self.index_in_file = int(self.index_in_file)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class RepositoryIdSource(Source):
    """
    Represents the source of a sequence that is identified by a repository id
    """

    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SHAREYOURCLONING_LINKML["RepositoryIdSource"]
    class_class_curie: ClassVar[str] = "shareyourcloning_linkml:RepositoryIdSource"
    class_name: ClassVar[str] = "RepositoryIdSource"
    class_model_uri: ClassVar[URIRef] = SHAREYOURCLONING_LINKML.RepositoryIdSource

    id: Union[int, RepositoryIdSourceId] = None
    repository_name: Union[str, "RepositoryName"] = None
    repository_id: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RepositoryIdSourceId):
            self.id = RepositoryIdSourceId(self.id)

        if self._is_empty(self.repository_name):
            self.MissingRequiredField("repository_name")
        if not isinstance(self.repository_name, RepositoryName):
            self.repository_name = RepositoryName(self.repository_name)

        if self._is_empty(self.repository_id):
            self.MissingRequiredField("repository_id")
        if not isinstance(self.repository_id, str):
            self.repository_id = str(self.repository_id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class AddGeneIdSource(RepositoryIdSource):
    """
    Represents the source of a sequence that is identified by an AddGene id
    """

    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SHAREYOURCLONING_LINKML["AddGeneIdSource"]
    class_class_curie: ClassVar[str] = "shareyourcloning_linkml:AddGeneIdSource"
    class_name: ClassVar[str] = "AddGeneIdSource"
    class_model_uri: ClassVar[URIRef] = SHAREYOURCLONING_LINKML.AddGeneIdSource

    id: Union[int, AddGeneIdSourceId] = None
    repository_name: Union[str, "RepositoryName"] = None
    repository_id: str = None
    sequence_file_url: Optional[str] = None
    addgene_sequence_type: Optional[Union[str, "AddGeneSequenceType"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AddGeneIdSourceId):
            self.id = AddGeneIdSourceId(self.id)

        if self.sequence_file_url is not None and not isinstance(self.sequence_file_url, str):
            self.sequence_file_url = str(self.sequence_file_url)

        if self.addgene_sequence_type is not None and not isinstance(self.addgene_sequence_type, AddGeneSequenceType):
            self.addgene_sequence_type = AddGeneSequenceType(self.addgene_sequence_type)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class GenomeCoordinatesSource(Source):
    """
    Represents the source of a sequence that is identified by genome coordinates, requested from NCBI
    """

    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SHAREYOURCLONING_LINKML["GenomeCoordinatesSource"]
    class_class_curie: ClassVar[str] = "shareyourcloning_linkml:GenomeCoordinatesSource"
    class_name: ClassVar[str] = "GenomeCoordinatesSource"
    class_model_uri: ClassVar[URIRef] = SHAREYOURCLONING_LINKML.GenomeCoordinatesSource

    id: Union[int, GenomeCoordinatesSourceId] = None
    sequence_accession: str = None
    start: int = None
    end: int = None
    strand: int = None
    assembly_accession: Optional[str] = None
    locus_tag: Optional[str] = None
    gene_id: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GenomeCoordinatesSourceId):
            self.id = GenomeCoordinatesSourceId(self.id)

        if self._is_empty(self.sequence_accession):
            self.MissingRequiredField("sequence_accession")
        if not isinstance(self.sequence_accession, str):
            self.sequence_accession = str(self.sequence_accession)

        if self._is_empty(self.start):
            self.MissingRequiredField("start")
        if not isinstance(self.start, int):
            self.start = int(self.start)

        if self._is_empty(self.end):
            self.MissingRequiredField("end")
        if not isinstance(self.end, int):
            self.end = int(self.end)

        if self._is_empty(self.strand):
            self.MissingRequiredField("strand")
        if not isinstance(self.strand, int):
            self.strand = int(self.strand)

        if self.assembly_accession is not None and not isinstance(self.assembly_accession, str):
            self.assembly_accession = str(self.assembly_accession)

        if self.locus_tag is not None and not isinstance(self.locus_tag, str):
            self.locus_tag = str(self.locus_tag)

        if self.gene_id is not None and not isinstance(self.gene_id, int):
            self.gene_id = int(self.gene_id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class SequenceCutSource(Source):
    """
    Represents the source of a sequence that is a subfragment of another sequence, generated by sequence cutting.
    """

    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SHAREYOURCLONING_LINKML["SequenceCutSource"]
    class_class_curie: ClassVar[str] = "shareyourcloning_linkml:SequenceCutSource"
    class_name: ClassVar[str] = "SequenceCutSource"
    class_model_uri: ClassVar[URIRef] = SHAREYOURCLONING_LINKML.SequenceCutSource

    id: Union[int, SequenceCutSourceId] = None
    left_edge: Optional[Union[dict, SequenceCut]] = None
    right_edge: Optional[Union[dict, SequenceCut]] = None
    input: Optional[Union[Union[int, SequenceId], List[Union[int, SequenceId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SequenceCutSourceId):
            self.id = SequenceCutSourceId(self.id)

        if self.left_edge is not None and not isinstance(self.left_edge, SequenceCut):
            self.left_edge = SequenceCut(**as_dict(self.left_edge))

        if self.right_edge is not None and not isinstance(self.right_edge, SequenceCut):
            self.right_edge = SequenceCut(**as_dict(self.right_edge))

        if not isinstance(self.input, list):
            self.input = [self.input] if self.input is not None else []
        self.input = [v if isinstance(v, SequenceId) else SequenceId(v) for v in self.input]

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class RestrictionEnzymeDigestionSource(SequenceCutSource):
    """
    Represents the source of a sequence that is a subfragment of another sequence, generated by sequence cutting using
    restriction enzymes.
    """

    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SHAREYOURCLONING_LINKML["RestrictionEnzymeDigestionSource"]
    class_class_curie: ClassVar[str] = "shareyourcloning_linkml:RestrictionEnzymeDigestionSource"
    class_name: ClassVar[str] = "RestrictionEnzymeDigestionSource"
    class_model_uri: ClassVar[URIRef] = SHAREYOURCLONING_LINKML.RestrictionEnzymeDigestionSource

    id: Union[int, RestrictionEnzymeDigestionSourceId] = None
    left_edge: Optional[Union[dict, RestrictionSequenceCut]] = None
    right_edge: Optional[Union[dict, RestrictionSequenceCut]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RestrictionEnzymeDigestionSourceId):
            self.id = RestrictionEnzymeDigestionSourceId(self.id)

        if self.left_edge is not None and not isinstance(self.left_edge, RestrictionSequenceCut):
            self.left_edge = RestrictionSequenceCut(**as_dict(self.left_edge))

        if self.right_edge is not None and not isinstance(self.right_edge, RestrictionSequenceCut):
            self.right_edge = RestrictionSequenceCut(**as_dict(self.right_edge))

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class SimpleSequenceLocation(YAMLRoot):
    """
    Represents a location within a sequence, for now support for ranges only
    """

    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SHAREYOURCLONING_LINKML["SimpleSequenceLocation"]
    class_class_curie: ClassVar[str] = "shareyourcloning_linkml:SimpleSequenceLocation"
    class_name: ClassVar[str] = "SimpleSequenceLocation"
    class_model_uri: ClassVar[URIRef] = SHAREYOURCLONING_LINKML.SimpleSequenceLocation

    start: int = None
    end: int = None
    strand: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.start):
            self.MissingRequiredField("start")
        if not isinstance(self.start, int):
            self.start = int(self.start)

        if self._is_empty(self.end):
            self.MissingRequiredField("end")
        if not isinstance(self.end, int):
            self.end = int(self.end)

        if self.strand is not None and not isinstance(self.strand, int):
            self.strand = int(self.strand)

        super().__post_init__(**kwargs)


@dataclass
class AssemblyJoinComponent(YAMLRoot):
    """
    Represents a component of a join between two fragments in an assembly
    """

    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SHAREYOURCLONING_LINKML["AssemblyJoinComponent"]
    class_class_curie: ClassVar[str] = "shareyourcloning_linkml:AssemblyJoinComponent"
    class_name: ClassVar[str] = "AssemblyJoinComponent"
    class_model_uri: ClassVar[URIRef] = SHAREYOURCLONING_LINKML.AssemblyJoinComponent

    sequence: Union[int, SequenceId] = None
    location: Union[dict, SimpleSequenceLocation] = None
    reverse_complemented: Union[bool, Bool] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.sequence):
            self.MissingRequiredField("sequence")
        if not isinstance(self.sequence, SequenceId):
            self.sequence = SequenceId(self.sequence)

        if self._is_empty(self.location):
            self.MissingRequiredField("location")
        if not isinstance(self.location, SimpleSequenceLocation):
            self.location = SimpleSequenceLocation(**as_dict(self.location))

        if self._is_empty(self.reverse_complemented):
            self.MissingRequiredField("reverse_complemented")
        if not isinstance(self.reverse_complemented, Bool):
            self.reverse_complemented = Bool(self.reverse_complemented)

        super().__post_init__(**kwargs)


@dataclass
class AssemblyJoin(YAMLRoot):
    """
    Represents a joint between two fragments in an assembly
    """

    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SHAREYOURCLONING_LINKML["AssemblyJoin"]
    class_class_curie: ClassVar[str] = "shareyourcloning_linkml:AssemblyJoin"
    class_name: ClassVar[str] = "AssemblyJoin"
    class_model_uri: ClassVar[URIRef] = SHAREYOURCLONING_LINKML.AssemblyJoin

    left: Union[dict, AssemblyJoinComponent] = None
    right: Union[dict, AssemblyJoinComponent] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.left):
            self.MissingRequiredField("left")
        if not isinstance(self.left, AssemblyJoinComponent):
            self.left = AssemblyJoinComponent(**as_dict(self.left))

        if self._is_empty(self.right):
            self.MissingRequiredField("right")
        if not isinstance(self.right, AssemblyJoinComponent):
            self.right = AssemblyJoinComponent(**as_dict(self.right))

        super().__post_init__(**kwargs)


@dataclass
class AssemblySource(Source):
    """
    Represents the source of a sequence that is an assembly of other sequences
    """

    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SHAREYOURCLONING_LINKML["AssemblySource"]
    class_class_curie: ClassVar[str] = "shareyourcloning_linkml:AssemblySource"
    class_name: ClassVar[str] = "AssemblySource"
    class_model_uri: ClassVar[URIRef] = SHAREYOURCLONING_LINKML.AssemblySource

    id: Union[int, AssemblySourceId] = None
    assembly: Union[Union[dict, AssemblyJoin], List[Union[dict, AssemblyJoin]]] = None
    circular: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AssemblySourceId):
            self.id = AssemblySourceId(self.id)

        if self._is_empty(self.assembly):
            self.MissingRequiredField("assembly")
        if not isinstance(self.assembly, list):
            self.assembly = [self.assembly] if self.assembly is not None else []
        self.assembly = [v if isinstance(v, AssemblyJoin) else AssemblyJoin(**as_dict(v)) for v in self.assembly]

        if self.circular is not None and not isinstance(self.circular, Bool):
            self.circular = Bool(self.circular)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class PCRSource(AssemblySource):
    """
    Represents the source of a sequence that is generated by PCR
    """

    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SHAREYOURCLONING_LINKML["PCRSource"]
    class_class_curie: ClassVar[str] = "shareyourcloning_linkml:PCRSource"
    class_name: ClassVar[str] = "PCRSource"
    class_model_uri: ClassVar[URIRef] = SHAREYOURCLONING_LINKML.PCRSource

    id: Union[int, PCRSourceId] = None
    assembly: Union[Union[dict, AssemblyJoin], List[Union[dict, AssemblyJoin]]] = None
    forward_primer: Union[int, PrimerId] = None
    reverse_primer: Union[int, PrimerId] = None
    input: Optional[Union[Union[int, SequenceId], List[Union[int, SequenceId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PCRSourceId):
            self.id = PCRSourceId(self.id)

        if self._is_empty(self.forward_primer):
            self.MissingRequiredField("forward_primer")
        if not isinstance(self.forward_primer, PrimerId):
            self.forward_primer = PrimerId(self.forward_primer)

        if self._is_empty(self.reverse_primer):
            self.MissingRequiredField("reverse_primer")
        if not isinstance(self.reverse_primer, PrimerId):
            self.reverse_primer = PrimerId(self.reverse_primer)

        if not isinstance(self.input, list):
            self.input = [self.input] if self.input is not None else []
        self.input = [v if isinstance(v, SequenceId) else SequenceId(v) for v in self.input]

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class LigationSource(AssemblySource):
    """
    Represents the source of a sequence that is generated by ligation with sticky or blunt ends.
    """

    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SHAREYOURCLONING_LINKML["LigationSource"]
    class_class_curie: ClassVar[str] = "shareyourcloning_linkml:LigationSource"
    class_name: ClassVar[str] = "LigationSource"
    class_model_uri: ClassVar[URIRef] = SHAREYOURCLONING_LINKML.LigationSource

    id: Union[int, LigationSourceId] = None
    assembly: Union[Union[dict, AssemblyJoin], List[Union[dict, AssemblyJoin]]] = None
    input: Optional[Union[Union[int, SequenceId], List[Union[int, SequenceId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, LigationSourceId):
            self.id = LigationSourceId(self.id)

        if not isinstance(self.input, list):
            self.input = [self.input] if self.input is not None else []
        self.input = [v if isinstance(v, SequenceId) else SequenceId(v) for v in self.input]

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class HomologousRecombinationSource(AssemblySource):
    """
    Represents the source of a sequence that is generated by homologous recombination
    """

    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SHAREYOURCLONING_LINKML["HomologousRecombinationSource"]
    class_class_curie: ClassVar[str] = "shareyourcloning_linkml:HomologousRecombinationSource"
    class_name: ClassVar[str] = "HomologousRecombinationSource"
    class_model_uri: ClassVar[URIRef] = SHAREYOURCLONING_LINKML.HomologousRecombinationSource

    id: Union[int, HomologousRecombinationSourceId] = None
    assembly: Union[Union[dict, AssemblyJoin], List[Union[dict, AssemblyJoin]]] = None
    input: Optional[Union[Union[int, SequenceId], List[Union[int, SequenceId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, HomologousRecombinationSourceId):
            self.id = HomologousRecombinationSourceId(self.id)

        if not isinstance(self.input, list):
            self.input = [self.input] if self.input is not None else []
        self.input = [v if isinstance(v, SequenceId) else SequenceId(v) for v in self.input]

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class GibsonAssemblySource(AssemblySource):
    """
    Represents the source of a sequence that is generated by Gibson assembly
    """

    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SHAREYOURCLONING_LINKML["GibsonAssemblySource"]
    class_class_curie: ClassVar[str] = "shareyourcloning_linkml:GibsonAssemblySource"
    class_name: ClassVar[str] = "GibsonAssemblySource"
    class_model_uri: ClassVar[URIRef] = SHAREYOURCLONING_LINKML.GibsonAssemblySource

    id: Union[int, GibsonAssemblySourceId] = None
    assembly: Union[Union[dict, AssemblyJoin], List[Union[dict, AssemblyJoin]]] = None
    input: Optional[Union[Union[int, SequenceId], List[Union[int, SequenceId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GibsonAssemblySourceId):
            self.id = GibsonAssemblySourceId(self.id)

        if not isinstance(self.input, list):
            self.input = [self.input] if self.input is not None else []
        self.input = [v if isinstance(v, SequenceId) else SequenceId(v) for v in self.input]

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class RestrictionAndLigationSource(AssemblySource):
    """
    Represents the source of a sequence that is generated by restriction and ligation
    """

    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SHAREYOURCLONING_LINKML["RestrictionAndLigationSource"]
    class_class_curie: ClassVar[str] = "shareyourcloning_linkml:RestrictionAndLigationSource"
    class_name: ClassVar[str] = "RestrictionAndLigationSource"
    class_model_uri: ClassVar[URIRef] = SHAREYOURCLONING_LINKML.RestrictionAndLigationSource

    id: Union[int, RestrictionAndLigationSourceId] = None
    assembly: Union[Union[dict, AssemblyJoin], List[Union[dict, AssemblyJoin]]] = None
    restriction_enzymes: Union[str, List[str]] = None
    input: Optional[Union[Union[int, SequenceId], List[Union[int, SequenceId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RestrictionAndLigationSourceId):
            self.id = RestrictionAndLigationSourceId(self.id)

        if self._is_empty(self.restriction_enzymes):
            self.MissingRequiredField("restriction_enzymes")
        if not isinstance(self.restriction_enzymes, list):
            self.restriction_enzymes = [self.restriction_enzymes] if self.restriction_enzymes is not None else []
        self.restriction_enzymes = [v if isinstance(v, str) else str(v) for v in self.restriction_enzymes]

        if not isinstance(self.input, list):
            self.input = [self.input] if self.input is not None else []
        self.input = [v if isinstance(v, SequenceId) else SequenceId(v) for v in self.input]

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class CRISPRSource(HomologousRecombinationSource):
    """
    Represents the source of a sequence that is generated by CRISPR
    """

    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SHAREYOURCLONING_LINKML["CRISPRSource"]
    class_class_curie: ClassVar[str] = "shareyourcloning_linkml:CRISPRSource"
    class_name: ClassVar[str] = "CRISPRSource"
    class_model_uri: ClassVar[URIRef] = SHAREYOURCLONING_LINKML.CRISPRSource

    id: Union[int, CRISPRSourceId] = None
    assembly: Union[Union[dict, AssemblyJoin], List[Union[dict, AssemblyJoin]]] = None
    guides: Union[Union[int, PrimerId], List[Union[int, PrimerId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CRISPRSourceId):
            self.id = CRISPRSourceId(self.id)

        if self._is_empty(self.guides):
            self.MissingRequiredField("guides")
        if not isinstance(self.guides, list):
            self.guides = [self.guides] if self.guides is not None else []
        self.guides = [v if isinstance(v, PrimerId) else PrimerId(v) for v in self.guides]

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class OligoHybridizationSource(Source):
    """
    Represents the source of a sequence that is generated by oligo hybridization
    """

    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SHAREYOURCLONING_LINKML["OligoHybridizationSource"]
    class_class_curie: ClassVar[str] = "shareyourcloning_linkml:OligoHybridizationSource"
    class_name: ClassVar[str] = "OligoHybridizationSource"
    class_model_uri: ClassVar[URIRef] = SHAREYOURCLONING_LINKML.OligoHybridizationSource

    id: Union[int, OligoHybridizationSourceId] = None
    forward_oligo: Union[int, PrimerId] = None
    reverse_oligo: Union[int, PrimerId] = None
    overhang_crick_3prime: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OligoHybridizationSourceId):
            self.id = OligoHybridizationSourceId(self.id)

        if self._is_empty(self.forward_oligo):
            self.MissingRequiredField("forward_oligo")
        if not isinstance(self.forward_oligo, PrimerId):
            self.forward_oligo = PrimerId(self.forward_oligo)

        if self._is_empty(self.reverse_oligo):
            self.MissingRequiredField("reverse_oligo")
        if not isinstance(self.reverse_oligo, PrimerId):
            self.reverse_oligo = PrimerId(self.reverse_oligo)

        if self.overhang_crick_3prime is not None and not isinstance(self.overhang_crick_3prime, int):
            self.overhang_crick_3prime = int(self.overhang_crick_3prime)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class PolymeraseExtensionSource(Source):
    """
    Represents the source of a sequence that is generated by polymerase extension
    """

    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SHAREYOURCLONING_LINKML["PolymeraseExtensionSource"]
    class_class_curie: ClassVar[str] = "shareyourcloning_linkml:PolymeraseExtensionSource"
    class_name: ClassVar[str] = "PolymeraseExtensionSource"
    class_model_uri: ClassVar[URIRef] = SHAREYOURCLONING_LINKML.PolymeraseExtensionSource

    id: Union[int, PolymeraseExtensionSourceId] = None
    input: Optional[Union[Union[int, SequenceId], List[Union[int, SequenceId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PolymeraseExtensionSourceId):
            self.id = PolymeraseExtensionSourceId(self.id)

        if not isinstance(self.input, list):
            self.input = [self.input] if self.input is not None else []
        self.input = [v if isinstance(v, SequenceId) else SequenceId(v) for v in self.input]

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class CloningStrategy(YAMLRoot):
    """
    Represents a cloning strategy
    """

    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SHAREYOURCLONING_LINKML["CloningStrategy"]
    class_class_curie: ClassVar[str] = "shareyourcloning_linkml:CloningStrategy"
    class_name: ClassVar[str] = "CloningStrategy"
    class_model_uri: ClassVar[URIRef] = SHAREYOURCLONING_LINKML.CloningStrategy

    sequences: Union[Dict[Union[int, SequenceId], Union[dict, Sequence]], List[Union[dict, Sequence]]] = empty_dict()
    sources: Union[Dict[Union[int, SourceId], Union[dict, Source]], List[Union[dict, Source]]] = empty_dict()
    primers: Optional[Union[Dict[Union[int, PrimerId], Union[dict, Primer]], List[Union[dict, Primer]]]] = empty_dict()
    description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.sequences):
            self.MissingRequiredField("sequences")
        self._normalize_inlined_as_list(slot_name="sequences", slot_type=Sequence, key_name="id", keyed=True)

        if self._is_empty(self.sources):
            self.MissingRequiredField("sources")
        self._normalize_inlined_as_list(slot_name="sources", slot_type=Source, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="primers", slot_type=Primer, key_name="id", keyed=True)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


# Enumerations
class RepositoryName(EnumDefinitionImpl):

    addgene = PermissibleValue(text="addgene", description="Addgene")
    genbank = PermissibleValue(text="genbank", description="GenBank")

    _defn = EnumDefinition(
        name="RepositoryName",
    )


class SequenceFileFormat(EnumDefinitionImpl):

    fasta = PermissibleValue(text="fasta")
    genbank = PermissibleValue(text="genbank")
    snapgene = PermissibleValue(text="snapgene")

    _defn = EnumDefinition(
        name="SequenceFileFormat",
    )


class AddGeneSequenceType(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="AddGeneSequenceType",
    )

    @classmethod
    def _addvals(cls):
        setattr(
            cls,
            "depositor-full",
            PermissibleValue(
                text="depositor-full", description="Full sequence of the plasmid submitted by the depositor"
            ),
        )
        setattr(
            cls,
            "addgene-full",
            PermissibleValue(text="addgene-full", description="Full sequence of the plasmid performed by Addgene"),
        )


# Slots
class slots:
    pass


slots.id = Slot(
    uri=SCHEMA.identifier,
    name="id",
    curie=SCHEMA.curie("identifier"),
    model_uri=SHAREYOURCLONING_LINKML.id,
    domain=None,
    range=URIRef,
)

slots.name = Slot(
    uri=SCHEMA.name,
    name="name",
    curie=SCHEMA.curie("name"),
    model_uri=SHAREYOURCLONING_LINKML.name,
    domain=None,
    range=Optional[str],
)

slots.restriction_enzyme = Slot(
    uri=SHAREYOURCLONING_LINKML.restriction_enzyme,
    name="restriction_enzyme",
    curie=SHAREYOURCLONING_LINKML.curie("restriction_enzyme"),
    model_uri=SHAREYOURCLONING_LINKML.restriction_enzyme,
    domain=None,
    range=Optional[str],
)

slots.restriction_enzymes = Slot(
    uri=SHAREYOURCLONING_LINKML.restriction_enzymes,
    name="restriction_enzymes",
    curie=SHAREYOURCLONING_LINKML.curie("restriction_enzymes"),
    model_uri=SHAREYOURCLONING_LINKML.restriction_enzymes,
    domain=None,
    range=Optional[Union[str, List[str]]],
)

slots.input = Slot(
    uri=SHAREYOURCLONING_LINKML.input,
    name="input",
    curie=SHAREYOURCLONING_LINKML.curie("input"),
    model_uri=SHAREYOURCLONING_LINKML.input,
    domain=None,
    range=Optional[Union[Union[int, SequenceId], List[Union[int, SequenceId]]]],
)

slots.output = Slot(
    uri=SHAREYOURCLONING_LINKML.output,
    name="output",
    curie=SHAREYOURCLONING_LINKML.curie("output"),
    model_uri=SHAREYOURCLONING_LINKML.output,
    domain=None,
    range=Optional[Union[int, SequenceId]],
)

slots.type = Slot(
    uri=SHAREYOURCLONING_LINKML.type,
    name="type",
    curie=SHAREYOURCLONING_LINKML.curie("type"),
    model_uri=SHAREYOURCLONING_LINKML.type,
    domain=None,
    range=Optional[str],
)

slots.sequence_file_format = Slot(
    uri=SHAREYOURCLONING_LINKML.sequence_file_format,
    name="sequence_file_format",
    curie=SHAREYOURCLONING_LINKML.curie("sequence_file_format"),
    model_uri=SHAREYOURCLONING_LINKML.sequence_file_format,
    domain=None,
    range=Optional[Union[str, "SequenceFileFormat"]],
)

slots.overhang_crick_3prime = Slot(
    uri=SHAREYOURCLONING_LINKML.overhang_crick_3prime,
    name="overhang_crick_3prime",
    curie=SHAREYOURCLONING_LINKML.curie("overhang_crick_3prime"),
    model_uri=SHAREYOURCLONING_LINKML.overhang_crick_3prime,
    domain=None,
    range=Optional[int],
)

slots.overhang_watson_3prime = Slot(
    uri=SHAREYOURCLONING_LINKML.overhang_watson_3prime,
    name="overhang_watson_3prime",
    curie=SHAREYOURCLONING_LINKML.curie("overhang_watson_3prime"),
    model_uri=SHAREYOURCLONING_LINKML.overhang_watson_3prime,
    domain=None,
    range=Optional[int],
)

slots.sequence_file_url = Slot(
    uri=SHAREYOURCLONING_LINKML.sequence_file_url,
    name="sequence_file_url",
    curie=SHAREYOURCLONING_LINKML.curie("sequence_file_url"),
    model_uri=SHAREYOURCLONING_LINKML.sequence_file_url,
    domain=None,
    range=Optional[str],
    pattern=re.compile(
        r"^https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)$"
    ),
)

slots.textFileSequence__file_content = Slot(
    uri=SHAREYOURCLONING_LINKML.file_content,
    name="textFileSequence__file_content",
    curie=SHAREYOURCLONING_LINKML.curie("file_content"),
    model_uri=SHAREYOURCLONING_LINKML.textFileSequence__file_content,
    domain=None,
    range=Optional[str],
)

slots.primer__sequence = Slot(
    uri=SHAREYOURCLONING_LINKML.sequence,
    name="primer__sequence",
    curie=SHAREYOURCLONING_LINKML.curie("sequence"),
    model_uri=SHAREYOURCLONING_LINKML.primer__sequence,
    domain=None,
    range=Optional[str],
    pattern=re.compile(r"^[acgtACGT]+$"),
)

slots.sequenceCut__cut_watson = Slot(
    uri=SHAREYOURCLONING_LINKML.cut_watson,
    name="sequenceCut__cut_watson",
    curie=SHAREYOURCLONING_LINKML.curie("cut_watson"),
    model_uri=SHAREYOURCLONING_LINKML.sequenceCut__cut_watson,
    domain=None,
    range=int,
)

slots.sequenceCut__overhang = Slot(
    uri=SHAREYOURCLONING_LINKML.overhang,
    name="sequenceCut__overhang",
    curie=SHAREYOURCLONING_LINKML.curie("overhang"),
    model_uri=SHAREYOURCLONING_LINKML.sequenceCut__overhang,
    domain=None,
    range=int,
)

slots.manuallyTypedSource__user_input = Slot(
    uri=SHAREYOURCLONING_LINKML.user_input,
    name="manuallyTypedSource__user_input",
    curie=SHAREYOURCLONING_LINKML.curie("user_input"),
    model_uri=SHAREYOURCLONING_LINKML.manuallyTypedSource__user_input,
    domain=None,
    range=str,
    pattern=re.compile(r"^[acgtACGT]+$"),
)

slots.manuallyTypedSource__circular = Slot(
    uri=SHAREYOURCLONING_LINKML.circular,
    name="manuallyTypedSource__circular",
    curie=SHAREYOURCLONING_LINKML.curie("circular"),
    model_uri=SHAREYOURCLONING_LINKML.manuallyTypedSource__circular,
    domain=None,
    range=Optional[Union[bool, Bool]],
)

slots.uploadedFileSource__file_name = Slot(
    uri=SHAREYOURCLONING_LINKML.file_name,
    name="uploadedFileSource__file_name",
    curie=SHAREYOURCLONING_LINKML.curie("file_name"),
    model_uri=SHAREYOURCLONING_LINKML.uploadedFileSource__file_name,
    domain=None,
    range=Optional[str],
)

slots.uploadedFileSource__index_in_file = Slot(
    uri=SHAREYOURCLONING_LINKML.index_in_file,
    name="uploadedFileSource__index_in_file",
    curie=SHAREYOURCLONING_LINKML.curie("index_in_file"),
    model_uri=SHAREYOURCLONING_LINKML.uploadedFileSource__index_in_file,
    domain=None,
    range=Optional[int],
)

slots.repositoryIdSource__repository_name = Slot(
    uri=SHAREYOURCLONING_LINKML.repository_name,
    name="repositoryIdSource__repository_name",
    curie=SHAREYOURCLONING_LINKML.curie("repository_name"),
    model_uri=SHAREYOURCLONING_LINKML.repositoryIdSource__repository_name,
    domain=None,
    range=Union[str, "RepositoryName"],
)

slots.repositoryIdSource__repository_id = Slot(
    uri=SHAREYOURCLONING_LINKML.repository_id,
    name="repositoryIdSource__repository_id",
    curie=SHAREYOURCLONING_LINKML.curie("repository_id"),
    model_uri=SHAREYOURCLONING_LINKML.repositoryIdSource__repository_id,
    domain=None,
    range=str,
)

slots.addGeneIdSource__addgene_sequence_type = Slot(
    uri=SHAREYOURCLONING_LINKML.addgene_sequence_type,
    name="addGeneIdSource__addgene_sequence_type",
    curie=SHAREYOURCLONING_LINKML.curie("addgene_sequence_type"),
    model_uri=SHAREYOURCLONING_LINKML.addGeneIdSource__addgene_sequence_type,
    domain=None,
    range=Optional[Union[str, "AddGeneSequenceType"]],
)

slots.genomeCoordinatesSource__assembly_accession = Slot(
    uri=SHAREYOURCLONING_LINKML.assembly_accession,
    name="genomeCoordinatesSource__assembly_accession",
    curie=SHAREYOURCLONING_LINKML.curie("assembly_accession"),
    model_uri=SHAREYOURCLONING_LINKML.genomeCoordinatesSource__assembly_accession,
    domain=None,
    range=Optional[str],
)

slots.genomeCoordinatesSource__sequence_accession = Slot(
    uri=SHAREYOURCLONING_LINKML.sequence_accession,
    name="genomeCoordinatesSource__sequence_accession",
    curie=SHAREYOURCLONING_LINKML.curie("sequence_accession"),
    model_uri=SHAREYOURCLONING_LINKML.genomeCoordinatesSource__sequence_accession,
    domain=None,
    range=str,
)

slots.genomeCoordinatesSource__locus_tag = Slot(
    uri=SHAREYOURCLONING_LINKML.locus_tag,
    name="genomeCoordinatesSource__locus_tag",
    curie=SHAREYOURCLONING_LINKML.curie("locus_tag"),
    model_uri=SHAREYOURCLONING_LINKML.genomeCoordinatesSource__locus_tag,
    domain=None,
    range=Optional[str],
)

slots.genomeCoordinatesSource__gene_id = Slot(
    uri=SHAREYOURCLONING_LINKML.gene_id,
    name="genomeCoordinatesSource__gene_id",
    curie=SHAREYOURCLONING_LINKML.curie("gene_id"),
    model_uri=SHAREYOURCLONING_LINKML.genomeCoordinatesSource__gene_id,
    domain=None,
    range=Optional[int],
)

slots.genomeCoordinatesSource__start = Slot(
    uri=SHAREYOURCLONING_LINKML.start,
    name="genomeCoordinatesSource__start",
    curie=SHAREYOURCLONING_LINKML.curie("start"),
    model_uri=SHAREYOURCLONING_LINKML.genomeCoordinatesSource__start,
    domain=None,
    range=int,
)

slots.genomeCoordinatesSource__end = Slot(
    uri=SHAREYOURCLONING_LINKML.end,
    name="genomeCoordinatesSource__end",
    curie=SHAREYOURCLONING_LINKML.curie("end"),
    model_uri=SHAREYOURCLONING_LINKML.genomeCoordinatesSource__end,
    domain=None,
    range=int,
)

slots.genomeCoordinatesSource__strand = Slot(
    uri=SHAREYOURCLONING_LINKML.strand,
    name="genomeCoordinatesSource__strand",
    curie=SHAREYOURCLONING_LINKML.curie("strand"),
    model_uri=SHAREYOURCLONING_LINKML.genomeCoordinatesSource__strand,
    domain=None,
    range=int,
)

slots.sequenceCutSource__left_edge = Slot(
    uri=SHAREYOURCLONING_LINKML.left_edge,
    name="sequenceCutSource__left_edge",
    curie=SHAREYOURCLONING_LINKML.curie("left_edge"),
    model_uri=SHAREYOURCLONING_LINKML.sequenceCutSource__left_edge,
    domain=None,
    range=Optional[Union[dict, SequenceCut]],
)

slots.sequenceCutSource__right_edge = Slot(
    uri=SHAREYOURCLONING_LINKML.right_edge,
    name="sequenceCutSource__right_edge",
    curie=SHAREYOURCLONING_LINKML.curie("right_edge"),
    model_uri=SHAREYOURCLONING_LINKML.sequenceCutSource__right_edge,
    domain=None,
    range=Optional[Union[dict, SequenceCut]],
)

slots.restrictionEnzymeDigestionSource__left_edge = Slot(
    uri=SHAREYOURCLONING_LINKML.left_edge,
    name="restrictionEnzymeDigestionSource__left_edge",
    curie=SHAREYOURCLONING_LINKML.curie("left_edge"),
    model_uri=SHAREYOURCLONING_LINKML.restrictionEnzymeDigestionSource__left_edge,
    domain=None,
    range=Optional[Union[dict, RestrictionSequenceCut]],
)

slots.restrictionEnzymeDigestionSource__right_edge = Slot(
    uri=SHAREYOURCLONING_LINKML.right_edge,
    name="restrictionEnzymeDigestionSource__right_edge",
    curie=SHAREYOURCLONING_LINKML.curie("right_edge"),
    model_uri=SHAREYOURCLONING_LINKML.restrictionEnzymeDigestionSource__right_edge,
    domain=None,
    range=Optional[Union[dict, RestrictionSequenceCut]],
)

slots.simpleSequenceLocation__start = Slot(
    uri=SHAREYOURCLONING_LINKML.start,
    name="simpleSequenceLocation__start",
    curie=SHAREYOURCLONING_LINKML.curie("start"),
    model_uri=SHAREYOURCLONING_LINKML.simpleSequenceLocation__start,
    domain=None,
    range=int,
)

slots.simpleSequenceLocation__end = Slot(
    uri=SHAREYOURCLONING_LINKML.end,
    name="simpleSequenceLocation__end",
    curie=SHAREYOURCLONING_LINKML.curie("end"),
    model_uri=SHAREYOURCLONING_LINKML.simpleSequenceLocation__end,
    domain=None,
    range=int,
)

slots.simpleSequenceLocation__strand = Slot(
    uri=SHAREYOURCLONING_LINKML.strand,
    name="simpleSequenceLocation__strand",
    curie=SHAREYOURCLONING_LINKML.curie("strand"),
    model_uri=SHAREYOURCLONING_LINKML.simpleSequenceLocation__strand,
    domain=None,
    range=Optional[int],
)

slots.assemblyJoinComponent__sequence = Slot(
    uri=SHAREYOURCLONING_LINKML.sequence,
    name="assemblyJoinComponent__sequence",
    curie=SHAREYOURCLONING_LINKML.curie("sequence"),
    model_uri=SHAREYOURCLONING_LINKML.assemblyJoinComponent__sequence,
    domain=None,
    range=Union[int, SequenceId],
)

slots.assemblyJoinComponent__location = Slot(
    uri=SHAREYOURCLONING_LINKML.location,
    name="assemblyJoinComponent__location",
    curie=SHAREYOURCLONING_LINKML.curie("location"),
    model_uri=SHAREYOURCLONING_LINKML.assemblyJoinComponent__location,
    domain=None,
    range=Union[dict, SimpleSequenceLocation],
)

slots.assemblyJoinComponent__reverse_complemented = Slot(
    uri=SHAREYOURCLONING_LINKML.reverse_complemented,
    name="assemblyJoinComponent__reverse_complemented",
    curie=SHAREYOURCLONING_LINKML.curie("reverse_complemented"),
    model_uri=SHAREYOURCLONING_LINKML.assemblyJoinComponent__reverse_complemented,
    domain=None,
    range=Union[bool, Bool],
)

slots.assemblyJoin__left = Slot(
    uri=SHAREYOURCLONING_LINKML.left,
    name="assemblyJoin__left",
    curie=SHAREYOURCLONING_LINKML.curie("left"),
    model_uri=SHAREYOURCLONING_LINKML.assemblyJoin__left,
    domain=None,
    range=Union[dict, AssemblyJoinComponent],
)

slots.assemblyJoin__right = Slot(
    uri=SHAREYOURCLONING_LINKML.right,
    name="assemblyJoin__right",
    curie=SHAREYOURCLONING_LINKML.curie("right"),
    model_uri=SHAREYOURCLONING_LINKML.assemblyJoin__right,
    domain=None,
    range=Union[dict, AssemblyJoinComponent],
)

slots.assemblySource__circular = Slot(
    uri=SHAREYOURCLONING_LINKML.circular,
    name="assemblySource__circular",
    curie=SHAREYOURCLONING_LINKML.curie("circular"),
    model_uri=SHAREYOURCLONING_LINKML.assemblySource__circular,
    domain=None,
    range=Optional[Union[bool, Bool]],
)

slots.assemblySource__assembly = Slot(
    uri=SHAREYOURCLONING_LINKML.assembly,
    name="assemblySource__assembly",
    curie=SHAREYOURCLONING_LINKML.curie("assembly"),
    model_uri=SHAREYOURCLONING_LINKML.assemblySource__assembly,
    domain=None,
    range=Union[Union[dict, AssemblyJoin], List[Union[dict, AssemblyJoin]]],
)

slots.pCRSource__forward_primer = Slot(
    uri=SHAREYOURCLONING_LINKML.forward_primer,
    name="pCRSource__forward_primer",
    curie=SHAREYOURCLONING_LINKML.curie("forward_primer"),
    model_uri=SHAREYOURCLONING_LINKML.pCRSource__forward_primer,
    domain=None,
    range=Union[int, PrimerId],
)

slots.pCRSource__reverse_primer = Slot(
    uri=SHAREYOURCLONING_LINKML.reverse_primer,
    name="pCRSource__reverse_primer",
    curie=SHAREYOURCLONING_LINKML.curie("reverse_primer"),
    model_uri=SHAREYOURCLONING_LINKML.pCRSource__reverse_primer,
    domain=None,
    range=Union[int, PrimerId],
)

slots.cRISPRSource__guides = Slot(
    uri=SHAREYOURCLONING_LINKML.guides,
    name="cRISPRSource__guides",
    curie=SHAREYOURCLONING_LINKML.curie("guides"),
    model_uri=SHAREYOURCLONING_LINKML.cRISPRSource__guides,
    domain=None,
    range=Union[Union[int, PrimerId], List[Union[int, PrimerId]]],
)

slots.oligoHybridizationSource__forward_oligo = Slot(
    uri=SHAREYOURCLONING_LINKML.forward_oligo,
    name="oligoHybridizationSource__forward_oligo",
    curie=SHAREYOURCLONING_LINKML.curie("forward_oligo"),
    model_uri=SHAREYOURCLONING_LINKML.oligoHybridizationSource__forward_oligo,
    domain=None,
    range=Union[int, PrimerId],
)

slots.oligoHybridizationSource__reverse_oligo = Slot(
    uri=SHAREYOURCLONING_LINKML.reverse_oligo,
    name="oligoHybridizationSource__reverse_oligo",
    curie=SHAREYOURCLONING_LINKML.curie("reverse_oligo"),
    model_uri=SHAREYOURCLONING_LINKML.oligoHybridizationSource__reverse_oligo,
    domain=None,
    range=Union[int, PrimerId],
)

slots.cloningStrategy__sequences = Slot(
    uri=SHAREYOURCLONING_LINKML.sequences,
    name="cloningStrategy__sequences",
    curie=SHAREYOURCLONING_LINKML.curie("sequences"),
    model_uri=SHAREYOURCLONING_LINKML.cloningStrategy__sequences,
    domain=None,
    range=Union[Dict[Union[int, SequenceId], Union[dict, Sequence]], List[Union[dict, Sequence]]],
)

slots.cloningStrategy__sources = Slot(
    uri=SHAREYOURCLONING_LINKML.sources,
    name="cloningStrategy__sources",
    curie=SHAREYOURCLONING_LINKML.curie("sources"),
    model_uri=SHAREYOURCLONING_LINKML.cloningStrategy__sources,
    domain=None,
    range=Union[Dict[Union[int, SourceId], Union[dict, Source]], List[Union[dict, Source]]],
)

slots.cloningStrategy__primers = Slot(
    uri=SHAREYOURCLONING_LINKML.primers,
    name="cloningStrategy__primers",
    curie=SHAREYOURCLONING_LINKML.curie("primers"),
    model_uri=SHAREYOURCLONING_LINKML.cloningStrategy__primers,
    domain=None,
    range=Optional[Union[Dict[Union[int, PrimerId], Union[dict, Primer]], List[Union[dict, Primer]]]],
)

slots.cloningStrategy__description = Slot(
    uri=SHAREYOURCLONING_LINKML.description,
    name="cloningStrategy__description",
    curie=SHAREYOURCLONING_LINKML.curie("description"),
    model_uri=SHAREYOURCLONING_LINKML.cloningStrategy__description,
    domain=None,
    range=Optional[str],
)

slots.TextFileSequence_sequence_file_format = Slot(
    uri=SHAREYOURCLONING_LINKML.sequence_file_format,
    name="TextFileSequence_sequence_file_format",
    curie=SHAREYOURCLONING_LINKML.curie("sequence_file_format"),
    model_uri=SHAREYOURCLONING_LINKML.TextFileSequence_sequence_file_format,
    domain=TextFileSequence,
    range=Union[str, "SequenceFileFormat"],
)

slots.TextFileSequence_overhang_crick_3prime = Slot(
    uri=SHAREYOURCLONING_LINKML.overhang_crick_3prime,
    name="TextFileSequence_overhang_crick_3prime",
    curie=SHAREYOURCLONING_LINKML.curie("overhang_crick_3prime"),
    model_uri=SHAREYOURCLONING_LINKML.TextFileSequence_overhang_crick_3prime,
    domain=TextFileSequence,
    range=Optional[int],
)

slots.TextFileSequence_overhang_watson_3prime = Slot(
    uri=SHAREYOURCLONING_LINKML.overhang_watson_3prime,
    name="TextFileSequence_overhang_watson_3prime",
    curie=SHAREYOURCLONING_LINKML.curie("overhang_watson_3prime"),
    model_uri=SHAREYOURCLONING_LINKML.TextFileSequence_overhang_watson_3prime,
    domain=TextFileSequence,
    range=Optional[int],
)

slots.RestrictionSequenceCut_restriction_enzyme = Slot(
    uri=SHAREYOURCLONING_LINKML.restriction_enzyme,
    name="RestrictionSequenceCut_restriction_enzyme",
    curie=SHAREYOURCLONING_LINKML.curie("restriction_enzyme"),
    model_uri=SHAREYOURCLONING_LINKML.RestrictionSequenceCut_restriction_enzyme,
    domain=RestrictionSequenceCut,
    range=str,
)

slots.ManuallyTypedSource_overhang_crick_3prime = Slot(
    uri=SHAREYOURCLONING_LINKML.overhang_crick_3prime,
    name="ManuallyTypedSource_overhang_crick_3prime",
    curie=SHAREYOURCLONING_LINKML.curie("overhang_crick_3prime"),
    model_uri=SHAREYOURCLONING_LINKML.ManuallyTypedSource_overhang_crick_3prime,
    domain=ManuallyTypedSource,
    range=Optional[int],
)

slots.ManuallyTypedSource_overhang_watson_3prime = Slot(
    uri=SHAREYOURCLONING_LINKML.overhang_watson_3prime,
    name="ManuallyTypedSource_overhang_watson_3prime",
    curie=SHAREYOURCLONING_LINKML.curie("overhang_watson_3prime"),
    model_uri=SHAREYOURCLONING_LINKML.ManuallyTypedSource_overhang_watson_3prime,
    domain=ManuallyTypedSource,
    range=Optional[int],
)

slots.UploadedFileSource_sequence_file_format = Slot(
    uri=SHAREYOURCLONING_LINKML.sequence_file_format,
    name="UploadedFileSource_sequence_file_format",
    curie=SHAREYOURCLONING_LINKML.curie("sequence_file_format"),
    model_uri=SHAREYOURCLONING_LINKML.UploadedFileSource_sequence_file_format,
    domain=UploadedFileSource,
    range=Union[str, "SequenceFileFormat"],
)

slots.SequenceCutSource_input = Slot(
    uri=SHAREYOURCLONING_LINKML.input,
    name="SequenceCutSource_input",
    curie=SHAREYOURCLONING_LINKML.curie("input"),
    model_uri=SHAREYOURCLONING_LINKML.SequenceCutSource_input,
    domain=SequenceCutSource,
    range=Optional[Union[Union[int, SequenceId], List[Union[int, SequenceId]]]],
)

slots.PCRSource_input = Slot(
    uri=SHAREYOURCLONING_LINKML.input,
    name="PCRSource_input",
    curie=SHAREYOURCLONING_LINKML.curie("input"),
    model_uri=SHAREYOURCLONING_LINKML.PCRSource_input,
    domain=PCRSource,
    range=Optional[Union[Union[int, SequenceId], List[Union[int, SequenceId]]]],
)

slots.LigationSource_input = Slot(
    uri=SHAREYOURCLONING_LINKML.input,
    name="LigationSource_input",
    curie=SHAREYOURCLONING_LINKML.curie("input"),
    model_uri=SHAREYOURCLONING_LINKML.LigationSource_input,
    domain=LigationSource,
    range=Optional[Union[Union[int, SequenceId], List[Union[int, SequenceId]]]],
)

slots.HomologousRecombinationSource_input = Slot(
    uri=SHAREYOURCLONING_LINKML.input,
    name="HomologousRecombinationSource_input",
    curie=SHAREYOURCLONING_LINKML.curie("input"),
    model_uri=SHAREYOURCLONING_LINKML.HomologousRecombinationSource_input,
    domain=HomologousRecombinationSource,
    range=Optional[Union[Union[int, SequenceId], List[Union[int, SequenceId]]]],
)

slots.GibsonAssemblySource_input = Slot(
    uri=SHAREYOURCLONING_LINKML.input,
    name="GibsonAssemblySource_input",
    curie=SHAREYOURCLONING_LINKML.curie("input"),
    model_uri=SHAREYOURCLONING_LINKML.GibsonAssemblySource_input,
    domain=GibsonAssemblySource,
    range=Optional[Union[Union[int, SequenceId], List[Union[int, SequenceId]]]],
)

slots.RestrictionAndLigationSource_restriction_enzymes = Slot(
    uri=SHAREYOURCLONING_LINKML.restriction_enzymes,
    name="RestrictionAndLigationSource_restriction_enzymes",
    curie=SHAREYOURCLONING_LINKML.curie("restriction_enzymes"),
    model_uri=SHAREYOURCLONING_LINKML.RestrictionAndLigationSource_restriction_enzymes,
    domain=RestrictionAndLigationSource,
    range=Union[str, List[str]],
)

slots.RestrictionAndLigationSource_input = Slot(
    uri=SHAREYOURCLONING_LINKML.input,
    name="RestrictionAndLigationSource_input",
    curie=SHAREYOURCLONING_LINKML.curie("input"),
    model_uri=SHAREYOURCLONING_LINKML.RestrictionAndLigationSource_input,
    domain=RestrictionAndLigationSource,
    range=Optional[Union[Union[int, SequenceId], List[Union[int, SequenceId]]]],
)

slots.PolymeraseExtensionSource_input = Slot(
    uri=SHAREYOURCLONING_LINKML.input,
    name="PolymeraseExtensionSource_input",
    curie=SHAREYOURCLONING_LINKML.curie("input"),
    model_uri=SHAREYOURCLONING_LINKML.PolymeraseExtensionSource_input,
    domain=PolymeraseExtensionSource,
    range=Optional[Union[Union[int, SequenceId], List[Union[int, SequenceId]]]],
)
