# Auto generated from shareyourcloning_linkml.yaml by pythongen.py version: 0.0.1
# Generation date: 2024-04-23T14:49:59
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
from linkml_runtime.linkml_model.types import Integer, String

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
OBI = CurieNamespace('OBI', 'http://purl.obolibrary.org/obo/OBI_')
PATO = CurieNamespace('PATO', 'http://purl.obolibrary.org/obo/PATO_')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/')
EXAMPLE = CurieNamespace('example', 'https://example.org/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
SHAREYOURCLONING_LINKML = CurieNamespace('shareyourcloning_linkml', 'https://w3id.org/genestorian/ShareYourCloning_LinkML/')
DEFAULT_ = SHAREYOURCLONING_LINKML


# Types

# Class references
class NamedThingId(extended_int):
    pass


class SequenceId(NamedThingId):
    pass


class TextFileSequenceId(SequenceId):
    pass


class PrimerId(NamedThingId):
    pass


class SequenceCutId(NamedThingId):
    pass


class RestrictionSequenceCutId(SequenceCutId):
    pass


class SourceId(NamedThingId):
    pass


class ManuallyTypedSourceId(SourceId):
    pass


class UploadedFileSourceId(SourceId):
    pass


class RepositoryIdSourceId(SourceId):
    pass


class GenomeCoordinatesSourceId(SourceId):
    pass


class CutSourceId(SourceId):
    pass


class RestrictionCutSourceId(CutSourceId):
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
class CloningStrategy(YAMLRoot):
    """
    Represents a cloning strategy
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SHAREYOURCLONING_LINKML["CloningStrategy"]
    class_class_curie: ClassVar[str] = "shareyourcloning_linkml:CloningStrategy"
    class_name: ClassVar[str] = "CloningStrategy"
    class_model_uri: ClassVar[URIRef] = SHAREYOURCLONING_LINKML.CloningStrategy

    sequences: Union[Union[int, SequenceId], List[Union[int, SequenceId]]] = None
    sources: Union[Union[int, SourceId], List[Union[int, SourceId]]] = None
    primers: Optional[Union[Union[int, PrimerId], List[Union[int, PrimerId]]]] = empty_list()
    description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.sequences):
            self.MissingRequiredField("sequences")
        if not isinstance(self.sequences, list):
            self.sequences = [self.sequences] if self.sequences is not None else []
        self.sequences = [v if isinstance(v, SequenceId) else SequenceId(v) for v in self.sequences]

        if self._is_empty(self.sources):
            self.MissingRequiredField("sources")
        if not isinstance(self.sources, list):
            self.sources = [self.sources] if self.sources is not None else []
        self.sources = [v if isinstance(v, SourceId) else SourceId(v) for v in self.sources]

        if not isinstance(self.primers, list):
            self.primers = [self.primers] if self.primers is not None else []
        self.primers = [v if isinstance(v, PrimerId) else PrimerId(v) for v in self.primers]

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

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
            return super().__new__(cls,*args,**kwargs)
        else:
            type_designator_value = kwargs[type_designator]
            target_cls = cls._class_for("class_name", type_designator_value)


            if target_cls is None:
                raise ValueError(f"Wrong type designator value: class {cls.__name__} "
                                 f"has no subclass with ['class_name']='{kwargs[type_designator]}'")
            return super().__new__(target_cls,*args,**kwargs)



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
    file_content: Optional[str] = None
    overhang_crick_3prime: Optional[int] = None
    overhang_watson_3prime: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TextFileSequenceId):
            self.id = TextFileSequenceId(self.id)

        if self._is_empty(self.sequence_file_format):
            self.MissingRequiredField("sequence_file_format")
        if not isinstance(self.sequence_file_format, SequenceFileFormat):
            self.sequence_file_format = SequenceFileFormat(self.sequence_file_format)

        if self.file_content is not None and not isinstance(self.file_content, str):
            self.file_content = str(self.file_content)

        if self.overhang_crick_3prime is not None and not isinstance(self.overhang_crick_3prime, int):
            self.overhang_crick_3prime = int(self.overhang_crick_3prime)

        if self.overhang_watson_3prime is not None and not isinstance(self.overhang_watson_3prime, int):
            self.overhang_watson_3prime = int(self.overhang_watson_3prime)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class Primer(NamedThing):
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


@dataclass
class SequenceCut(NamedThing):
    """
    Represents a cut in a DNA sequence
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SHAREYOURCLONING_LINKML["SequenceCut"]
    class_class_curie: ClassVar[str] = "shareyourcloning_linkml:SequenceCut"
    class_name: ClassVar[str] = "SequenceCut"
    class_model_uri: ClassVar[URIRef] = SHAREYOURCLONING_LINKML.SequenceCut

    id: Union[int, SequenceCutId] = None
    cut_watson: Optional[int] = None
    overhang: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SequenceCutId):
            self.id = SequenceCutId(self.id)

        if self.cut_watson is not None and not isinstance(self.cut_watson, int):
            self.cut_watson = int(self.cut_watson)

        if self.overhang is not None and not isinstance(self.overhang, int):
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

    id: Union[int, RestrictionSequenceCutId] = None
    restriction_enzyme: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RestrictionSequenceCutId):
            self.id = RestrictionSequenceCutId(self.id)

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
    input: Optional[Union[int, List[int]]] = empty_list()
    output: Optional[int] = None
    type: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.input, list):
            self.input = [self.input] if self.input is not None else []
        self.input = [v if isinstance(v, int) else int(v) for v in self.input]

        if self.output is not None and not isinstance(self.output, int):
            self.output = int(self.output)

        self.type = str(self.class_name)

        super().__post_init__(**kwargs)


    def __new__(cls, *args, **kwargs):

        type_designator = "type"
        if not type_designator in kwargs:
            return super().__new__(cls,*args,**kwargs)
        else:
            type_designator_value = kwargs[type_designator]
            target_cls = cls._class_for("class_name", type_designator_value)


            if target_cls is None:
                raise ValueError(f"Wrong type designator value: class {cls.__name__} "
                                 f"has no subclass with ['class_name']='{kwargs[type_designator]}'")
            return super().__new__(target_cls,*args,**kwargs)



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

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ManuallyTypedSourceId):
            self.id = ManuallyTypedSourceId(self.id)

        if self._is_empty(self.user_input):
            self.MissingRequiredField("user_input")
        if not isinstance(self.user_input, str):
            self.user_input = str(self.user_input)

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
    stop: int = None
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

        if self._is_empty(self.stop):
            self.MissingRequiredField("stop")
        if not isinstance(self.stop, int):
            self.stop = int(self.stop)

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
class CutSource(Source):
    """
    Represents the source of a sequence that is a subfragment of another sequence, generated by sequence cutting.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SHAREYOURCLONING_LINKML["CutSource"]
    class_class_curie: ClassVar[str] = "shareyourcloning_linkml:CutSource"
    class_name: ClassVar[str] = "CutSource"
    class_model_uri: ClassVar[URIRef] = SHAREYOURCLONING_LINKML.CutSource

    id: Union[int, CutSourceId] = None
    left_cut: Optional[Union[int, SequenceCutId]] = None
    right_cut: Optional[Union[int, SequenceCutId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CutSourceId):
            self.id = CutSourceId(self.id)

        if self.left_cut is not None and not isinstance(self.left_cut, SequenceCutId):
            self.left_cut = SequenceCutId(self.left_cut)

        if self.right_cut is not None and not isinstance(self.right_cut, SequenceCutId):
            self.right_cut = SequenceCutId(self.right_cut)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class RestrictionCutSource(CutSource):
    """
    Represents the source of a sequence that is a subfragment of another sequence, generated by sequence cutting using
    restriction enzymes.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SHAREYOURCLONING_LINKML["RestrictionCutSource"]
    class_class_curie: ClassVar[str] = "shareyourcloning_linkml:RestrictionCutSource"
    class_name: ClassVar[str] = "RestrictionCutSource"
    class_model_uri: ClassVar[URIRef] = SHAREYOURCLONING_LINKML.RestrictionCutSource

    id: Union[int, RestrictionCutSourceId] = None
    left_cut: Optional[Union[int, RestrictionSequenceCutId]] = None
    right_cut: Optional[Union[int, RestrictionSequenceCutId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RestrictionCutSourceId):
            self.id = RestrictionCutSourceId(self.id)

        if self.left_cut is not None and not isinstance(self.left_cut, RestrictionSequenceCutId):
            self.left_cut = RestrictionSequenceCutId(self.left_cut)

        if self.right_cut is not None and not isinstance(self.right_cut, RestrictionSequenceCutId):
            self.right_cut = RestrictionSequenceCutId(self.right_cut)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


# Enumerations
class RepositoryName(EnumDefinitionImpl):

    addgene = PermissibleValue(
        text="addgene",
        description="Addgene")
    genbank = PermissibleValue(
        text="genbank",
        description="GenBank")

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

# Slots
class slots:
    pass

slots.id = Slot(uri=SCHEMA.identifier, name="id", curie=SCHEMA.curie('identifier'),
                   model_uri=SHAREYOURCLONING_LINKML.id, domain=None, range=URIRef)

slots.name = Slot(uri=SCHEMA.name, name="name", curie=SCHEMA.curie('name'),
                   model_uri=SHAREYOURCLONING_LINKML.name, domain=None, range=Optional[str])

slots.restriction_enzyme = Slot(uri=SHAREYOURCLONING_LINKML.restriction_enzyme, name="restriction_enzyme", curie=SHAREYOURCLONING_LINKML.curie('restriction_enzyme'),
                   model_uri=SHAREYOURCLONING_LINKML.restriction_enzyme, domain=None, range=Optional[str])

slots.input = Slot(uri=SHAREYOURCLONING_LINKML.input, name="input", curie=SHAREYOURCLONING_LINKML.curie('input'),
                   model_uri=SHAREYOURCLONING_LINKML.input, domain=None, range=Optional[Union[int, List[int]]])

slots.output = Slot(uri=SHAREYOURCLONING_LINKML.output, name="output", curie=SHAREYOURCLONING_LINKML.curie('output'),
                   model_uri=SHAREYOURCLONING_LINKML.output, domain=None, range=Optional[int])

slots.type = Slot(uri=SHAREYOURCLONING_LINKML.type, name="type", curie=SHAREYOURCLONING_LINKML.curie('type'),
                   model_uri=SHAREYOURCLONING_LINKML.type, domain=None, range=Optional[str])

slots.sequence_file_format = Slot(uri=SHAREYOURCLONING_LINKML.sequence_file_format, name="sequence_file_format", curie=SHAREYOURCLONING_LINKML.curie('sequence_file_format'),
                   model_uri=SHAREYOURCLONING_LINKML.sequence_file_format, domain=None, range=Optional[Union[str, "SequenceFileFormat"]])

slots.cloningStrategy__sequences = Slot(uri=SHAREYOURCLONING_LINKML.sequences, name="cloningStrategy__sequences", curie=SHAREYOURCLONING_LINKML.curie('sequences'),
                   model_uri=SHAREYOURCLONING_LINKML.cloningStrategy__sequences, domain=None, range=Union[Union[int, SequenceId], List[Union[int, SequenceId]]])

slots.cloningStrategy__sources = Slot(uri=SHAREYOURCLONING_LINKML.sources, name="cloningStrategy__sources", curie=SHAREYOURCLONING_LINKML.curie('sources'),
                   model_uri=SHAREYOURCLONING_LINKML.cloningStrategy__sources, domain=None, range=Union[Union[int, SourceId], List[Union[int, SourceId]]])

slots.cloningStrategy__primers = Slot(uri=SHAREYOURCLONING_LINKML.primers, name="cloningStrategy__primers", curie=SHAREYOURCLONING_LINKML.curie('primers'),
                   model_uri=SHAREYOURCLONING_LINKML.cloningStrategy__primers, domain=None, range=Optional[Union[Union[int, PrimerId], List[Union[int, PrimerId]]]])

slots.cloningStrategy__description = Slot(uri=SHAREYOURCLONING_LINKML.description, name="cloningStrategy__description", curie=SHAREYOURCLONING_LINKML.curie('description'),
                   model_uri=SHAREYOURCLONING_LINKML.cloningStrategy__description, domain=None, range=Optional[str])

slots.textFileSequence__file_content = Slot(uri=SHAREYOURCLONING_LINKML.file_content, name="textFileSequence__file_content", curie=SHAREYOURCLONING_LINKML.curie('file_content'),
                   model_uri=SHAREYOURCLONING_LINKML.textFileSequence__file_content, domain=None, range=Optional[str])

slots.textFileSequence__overhang_crick_3prime = Slot(uri=SHAREYOURCLONING_LINKML.overhang_crick_3prime, name="textFileSequence__overhang_crick_3prime", curie=SHAREYOURCLONING_LINKML.curie('overhang_crick_3prime'),
                   model_uri=SHAREYOURCLONING_LINKML.textFileSequence__overhang_crick_3prime, domain=None, range=Optional[int])

slots.textFileSequence__overhang_watson_3prime = Slot(uri=SHAREYOURCLONING_LINKML.overhang_watson_3prime, name="textFileSequence__overhang_watson_3prime", curie=SHAREYOURCLONING_LINKML.curie('overhang_watson_3prime'),
                   model_uri=SHAREYOURCLONING_LINKML.textFileSequence__overhang_watson_3prime, domain=None, range=Optional[int])

slots.primer__sequence = Slot(uri=SHAREYOURCLONING_LINKML.sequence, name="primer__sequence", curie=SHAREYOURCLONING_LINKML.curie('sequence'),
                   model_uri=SHAREYOURCLONING_LINKML.primer__sequence, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[acgtACGT]+$'))

slots.sequenceCut__cut_watson = Slot(uri=SHAREYOURCLONING_LINKML.cut_watson, name="sequenceCut__cut_watson", curie=SHAREYOURCLONING_LINKML.curie('cut_watson'),
                   model_uri=SHAREYOURCLONING_LINKML.sequenceCut__cut_watson, domain=None, range=Optional[int])

slots.sequenceCut__overhang = Slot(uri=SHAREYOURCLONING_LINKML.overhang, name="sequenceCut__overhang", curie=SHAREYOURCLONING_LINKML.curie('overhang'),
                   model_uri=SHAREYOURCLONING_LINKML.sequenceCut__overhang, domain=None, range=Optional[int])

slots.manuallyTypedSource__user_input = Slot(uri=SHAREYOURCLONING_LINKML.user_input, name="manuallyTypedSource__user_input", curie=SHAREYOURCLONING_LINKML.curie('user_input'),
                   model_uri=SHAREYOURCLONING_LINKML.manuallyTypedSource__user_input, domain=None, range=str,
                   pattern=re.compile(r'^[acgtACGT]+$'))

slots.uploadedFileSource__file_name = Slot(uri=SHAREYOURCLONING_LINKML.file_name, name="uploadedFileSource__file_name", curie=SHAREYOURCLONING_LINKML.curie('file_name'),
                   model_uri=SHAREYOURCLONING_LINKML.uploadedFileSource__file_name, domain=None, range=Optional[str])

slots.uploadedFileSource__index_in_file = Slot(uri=SHAREYOURCLONING_LINKML.index_in_file, name="uploadedFileSource__index_in_file", curie=SHAREYOURCLONING_LINKML.curie('index_in_file'),
                   model_uri=SHAREYOURCLONING_LINKML.uploadedFileSource__index_in_file, domain=None, range=Optional[int])

slots.repositoryIdSource__repository_name = Slot(uri=SHAREYOURCLONING_LINKML.repository_name, name="repositoryIdSource__repository_name", curie=SHAREYOURCLONING_LINKML.curie('repository_name'),
                   model_uri=SHAREYOURCLONING_LINKML.repositoryIdSource__repository_name, domain=None, range=Union[str, "RepositoryName"])

slots.repositoryIdSource__repository_id = Slot(uri=SHAREYOURCLONING_LINKML.repository_id, name="repositoryIdSource__repository_id", curie=SHAREYOURCLONING_LINKML.curie('repository_id'),
                   model_uri=SHAREYOURCLONING_LINKML.repositoryIdSource__repository_id, domain=None, range=str)

slots.genomeCoordinatesSource__assembly_accession = Slot(uri=SHAREYOURCLONING_LINKML.assembly_accession, name="genomeCoordinatesSource__assembly_accession", curie=SHAREYOURCLONING_LINKML.curie('assembly_accession'),
                   model_uri=SHAREYOURCLONING_LINKML.genomeCoordinatesSource__assembly_accession, domain=None, range=Optional[str])

slots.genomeCoordinatesSource__sequence_accession = Slot(uri=SHAREYOURCLONING_LINKML.sequence_accession, name="genomeCoordinatesSource__sequence_accession", curie=SHAREYOURCLONING_LINKML.curie('sequence_accession'),
                   model_uri=SHAREYOURCLONING_LINKML.genomeCoordinatesSource__sequence_accession, domain=None, range=str)

slots.genomeCoordinatesSource__locus_tag = Slot(uri=SHAREYOURCLONING_LINKML.locus_tag, name="genomeCoordinatesSource__locus_tag", curie=SHAREYOURCLONING_LINKML.curie('locus_tag'),
                   model_uri=SHAREYOURCLONING_LINKML.genomeCoordinatesSource__locus_tag, domain=None, range=Optional[str])

slots.genomeCoordinatesSource__gene_id = Slot(uri=SHAREYOURCLONING_LINKML.gene_id, name="genomeCoordinatesSource__gene_id", curie=SHAREYOURCLONING_LINKML.curie('gene_id'),
                   model_uri=SHAREYOURCLONING_LINKML.genomeCoordinatesSource__gene_id, domain=None, range=Optional[int])

slots.genomeCoordinatesSource__start = Slot(uri=SHAREYOURCLONING_LINKML.start, name="genomeCoordinatesSource__start", curie=SHAREYOURCLONING_LINKML.curie('start'),
                   model_uri=SHAREYOURCLONING_LINKML.genomeCoordinatesSource__start, domain=None, range=int)

slots.genomeCoordinatesSource__stop = Slot(uri=SHAREYOURCLONING_LINKML.stop, name="genomeCoordinatesSource__stop", curie=SHAREYOURCLONING_LINKML.curie('stop'),
                   model_uri=SHAREYOURCLONING_LINKML.genomeCoordinatesSource__stop, domain=None, range=int)

slots.genomeCoordinatesSource__strand = Slot(uri=SHAREYOURCLONING_LINKML.strand, name="genomeCoordinatesSource__strand", curie=SHAREYOURCLONING_LINKML.curie('strand'),
                   model_uri=SHAREYOURCLONING_LINKML.genomeCoordinatesSource__strand, domain=None, range=int)

slots.cutSource__left_cut = Slot(uri=SHAREYOURCLONING_LINKML.left_cut, name="cutSource__left_cut", curie=SHAREYOURCLONING_LINKML.curie('left_cut'),
                   model_uri=SHAREYOURCLONING_LINKML.cutSource__left_cut, domain=None, range=Optional[Union[int, SequenceCutId]])

slots.cutSource__right_cut = Slot(uri=SHAREYOURCLONING_LINKML.right_cut, name="cutSource__right_cut", curie=SHAREYOURCLONING_LINKML.curie('right_cut'),
                   model_uri=SHAREYOURCLONING_LINKML.cutSource__right_cut, domain=None, range=Optional[Union[int, SequenceCutId]])

slots.restrictionCutSource__left_cut = Slot(uri=SHAREYOURCLONING_LINKML.left_cut, name="restrictionCutSource__left_cut", curie=SHAREYOURCLONING_LINKML.curie('left_cut'),
                   model_uri=SHAREYOURCLONING_LINKML.restrictionCutSource__left_cut, domain=None, range=Optional[Union[int, RestrictionSequenceCutId]])

slots.restrictionCutSource__right_cut = Slot(uri=SHAREYOURCLONING_LINKML.right_cut, name="restrictionCutSource__right_cut", curie=SHAREYOURCLONING_LINKML.curie('right_cut'),
                   model_uri=SHAREYOURCLONING_LINKML.restrictionCutSource__right_cut, domain=None, range=Optional[Union[int, RestrictionSequenceCutId]])

slots.TextFileSequence_sequence_file_format = Slot(uri=SHAREYOURCLONING_LINKML.sequence_file_format, name="TextFileSequence_sequence_file_format", curie=SHAREYOURCLONING_LINKML.curie('sequence_file_format'),
                   model_uri=SHAREYOURCLONING_LINKML.TextFileSequence_sequence_file_format, domain=TextFileSequence, range=Union[str, "SequenceFileFormat"])

slots.RestrictionSequenceCut_restriction_enzyme = Slot(uri=SHAREYOURCLONING_LINKML.restriction_enzyme, name="RestrictionSequenceCut_restriction_enzyme", curie=SHAREYOURCLONING_LINKML.curie('restriction_enzyme'),
                   model_uri=SHAREYOURCLONING_LINKML.RestrictionSequenceCut_restriction_enzyme, domain=RestrictionSequenceCut, range=str)

slots.UploadedFileSource_sequence_file_format = Slot(uri=SHAREYOURCLONING_LINKML.sequence_file_format, name="UploadedFileSource_sequence_file_format", curie=SHAREYOURCLONING_LINKML.curie('sequence_file_format'),
                   model_uri=SHAREYOURCLONING_LINKML.UploadedFileSource_sequence_file_format, domain=UploadedFileSource, range=Union[str, "SequenceFileFormat"])