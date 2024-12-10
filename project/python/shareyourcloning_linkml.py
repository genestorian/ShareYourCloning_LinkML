# Auto generated from shareyourcloning_linkml.yaml by pythongen.py version: 0.0.1
# Generation date: 2024-12-10T14:43:54
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
from datetime import date, datetime, time
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import Boolean, Float, Integer, String
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


class BenchlingUrlSourceId(RepositoryIdSourceId):
    pass


class SnapGenePlasmidSourceId(RepositoryIdSourceId):
    pass


class EuroscarfSourceId(RepositoryIdSourceId):
    pass


class IGEMSourceId(RepositoryIdSourceId):
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


class InFusionSourceId(AssemblySourceId):
    pass


class OverlapExtensionPCRLigationSourceId(AssemblySourceId):
    pass


class RestrictionAndLigationSourceId(AssemblySourceId):
    pass


class GatewaySourceId(AssemblySourceId):
    pass


class CRISPRSourceId(HomologousRecombinationSourceId):
    pass


class OligoHybridizationSourceId(SourceId):
    pass


class PolymeraseExtensionSourceId(SourceId):
    pass


class AnnotationSourceId(SourceId):
    pass


@dataclass(repr=False)
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


@dataclass(repr=False)
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


@dataclass(repr=False)
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


@dataclass(repr=False)
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


@dataclass(repr=False)
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


@dataclass(repr=False)
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


@dataclass(repr=False)
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
    output_name: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.input, list):
            self.input = [self.input] if self.input is not None else []
        self.input = [v if isinstance(v, SequenceId) else SequenceId(v) for v in self.input]

        if self.output is not None and not isinstance(self.output, SequenceId):
            self.output = SequenceId(self.output)

        self.type = str(self.class_name)

        if self.output_name is not None and not isinstance(self.output_name, str):
            self.output_name = str(self.output_name)

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


@dataclass(repr=False)
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


@dataclass(repr=False)
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
    circularize: Optional[Union[bool, Bool]] = None

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

        if self.circularize is not None and not isinstance(self.circularize, Bool):
            self.circularize = Bool(self.circularize)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
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
    repository_id: str = None
    repository_name: Union[str, "RepositoryName"] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RepositoryIdSourceId):
            self.id = RepositoryIdSourceId(self.id)

        if self._is_empty(self.repository_id):
            self.MissingRequiredField("repository_id")
        if not isinstance(self.repository_id, str):
            self.repository_id = str(self.repository_id)

        if self._is_empty(self.repository_name):
            self.MissingRequiredField("repository_name")
        if not isinstance(self.repository_name, RepositoryName):
            self.repository_name = RepositoryName(self.repository_name)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
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
    repository_id: str = None
    repository_name: Union[str, "RepositoryName"] = None
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


@dataclass(repr=False)
class BenchlingUrlSource(RepositoryIdSource):
    """
    Represents the source of a sequence that is identified by a Benchling URL
    """

    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SHAREYOURCLONING_LINKML["BenchlingUrlSource"]
    class_class_curie: ClassVar[str] = "shareyourcloning_linkml:BenchlingUrlSource"
    class_name: ClassVar[str] = "BenchlingUrlSource"
    class_model_uri: ClassVar[URIRef] = SHAREYOURCLONING_LINKML.BenchlingUrlSource

    id: Union[int, BenchlingUrlSourceId] = None
    repository_name: Union[str, "RepositoryName"] = None
    repository_id: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BenchlingUrlSourceId):
            self.id = BenchlingUrlSourceId(self.id)

        if self._is_empty(self.repository_id):
            self.MissingRequiredField("repository_id")
        if not isinstance(self.repository_id, str):
            self.repository_id = str(self.repository_id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class SnapGenePlasmidSource(RepositoryIdSource):
    """
    Represents the source of a sequence from the SnapGene plasmid library identified by a SnapGene subpath of
    https://www.snapgene.com/plasmids/
    """

    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SHAREYOURCLONING_LINKML["SnapGenePlasmidSource"]
    class_class_curie: ClassVar[str] = "shareyourcloning_linkml:SnapGenePlasmidSource"
    class_name: ClassVar[str] = "SnapGenePlasmidSource"
    class_model_uri: ClassVar[URIRef] = SHAREYOURCLONING_LINKML.SnapGenePlasmidSource

    id: Union[int, SnapGenePlasmidSourceId] = None
    repository_name: Union[str, "RepositoryName"] = None
    repository_id: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SnapGenePlasmidSourceId):
            self.id = SnapGenePlasmidSourceId(self.id)

        if self._is_empty(self.repository_id):
            self.MissingRequiredField("repository_id")
        if not isinstance(self.repository_id, str):
            self.repository_id = str(self.repository_id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class EuroscarfSource(RepositoryIdSource):
    """
    Represents the source of a sequence from the Euroscarf plasmid library
    """

    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SHAREYOURCLONING_LINKML["EuroscarfSource"]
    class_class_curie: ClassVar[str] = "shareyourcloning_linkml:EuroscarfSource"
    class_name: ClassVar[str] = "EuroscarfSource"
    class_model_uri: ClassVar[URIRef] = SHAREYOURCLONING_LINKML.EuroscarfSource

    id: Union[int, EuroscarfSourceId] = None
    repository_name: Union[str, "RepositoryName"] = None
    repository_id: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EuroscarfSourceId):
            self.id = EuroscarfSourceId(self.id)

        if self._is_empty(self.repository_id):
            self.MissingRequiredField("repository_id")
        if not isinstance(self.repository_id, str):
            self.repository_id = str(self.repository_id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class IGEMSource(RepositoryIdSource):
    """
    Represents the source of a sequence from an iGEM collection
    """

    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SHAREYOURCLONING_LINKML["IGEMSource"]
    class_class_curie: ClassVar[str] = "shareyourcloning_linkml:IGEMSource"
    class_name: ClassVar[str] = "IGEMSource"
    class_model_uri: ClassVar[URIRef] = SHAREYOURCLONING_LINKML.IGEMSource

    id: Union[int, IGEMSourceId] = None
    repository_name: Union[str, "RepositoryName"] = None
    sequence_file_url: str = None
    repository_id: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IGEMSourceId):
            self.id = IGEMSourceId(self.id)

        if self._is_empty(self.sequence_file_url):
            self.MissingRequiredField("sequence_file_url")
        if not isinstance(self.sequence_file_url, str):
            self.sequence_file_url = str(self.sequence_file_url)

        if self._is_empty(self.repository_id):
            self.MissingRequiredField("repository_id")
        if not isinstance(self.repository_id, str):
            self.repository_id = str(self.repository_id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
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


@dataclass(repr=False)
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

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SequenceCutSourceId):
            self.id = SequenceCutSourceId(self.id)

        if self.left_edge is not None and not isinstance(self.left_edge, SequenceCut):
            self.left_edge = SequenceCut(**as_dict(self.left_edge))

        if self.right_edge is not None and not isinstance(self.right_edge, SequenceCut):
            self.right_edge = SequenceCut(**as_dict(self.right_edge))

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
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


@dataclass(repr=False)
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


@dataclass(repr=False)
class AssemblyFragment(YAMLRoot):
    """
    Represents a fragment in an assembly
    """

    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SHAREYOURCLONING_LINKML["AssemblyFragment"]
    class_class_curie: ClassVar[str] = "shareyourcloning_linkml:AssemblyFragment"
    class_name: ClassVar[str] = "AssemblyFragment"
    class_model_uri: ClassVar[URIRef] = SHAREYOURCLONING_LINKML.AssemblyFragment

    sequence: Union[int, SequenceId] = None
    reverse_complemented: Union[bool, Bool] = None
    left_location: Optional[Union[dict, SimpleSequenceLocation]] = None
    right_location: Optional[Union[dict, SimpleSequenceLocation]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.sequence):
            self.MissingRequiredField("sequence")
        if not isinstance(self.sequence, SequenceId):
            self.sequence = SequenceId(self.sequence)

        if self._is_empty(self.reverse_complemented):
            self.MissingRequiredField("reverse_complemented")
        if not isinstance(self.reverse_complemented, Bool):
            self.reverse_complemented = Bool(self.reverse_complemented)

        if self.left_location is not None and not isinstance(self.left_location, SimpleSequenceLocation):
            self.left_location = SimpleSequenceLocation(**as_dict(self.left_location))

        if self.right_location is not None and not isinstance(self.right_location, SimpleSequenceLocation):
            self.right_location = SimpleSequenceLocation(**as_dict(self.right_location))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
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
    assembly: Union[Union[dict, AssemblyFragment], List[Union[dict, AssemblyFragment]]] = None
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
        self.assembly = [
            v if isinstance(v, AssemblyFragment) else AssemblyFragment(**as_dict(v)) for v in self.assembly
        ]

        if self.circular is not None and not isinstance(self.circular, Bool):
            self.circular = Bool(self.circular)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
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
    assembly: Union[Union[dict, AssemblyFragment], List[Union[dict, AssemblyFragment]]] = None
    add_primer_features: Optional[Union[bool, Bool]] = False

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PCRSourceId):
            self.id = PCRSourceId(self.id)

        if self.add_primer_features is not None and not isinstance(self.add_primer_features, Bool):
            self.add_primer_features = Bool(self.add_primer_features)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
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
    assembly: Union[Union[dict, AssemblyFragment], List[Union[dict, AssemblyFragment]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, LigationSourceId):
            self.id = LigationSourceId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
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
    assembly: Union[Union[dict, AssemblyFragment], List[Union[dict, AssemblyFragment]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, HomologousRecombinationSourceId):
            self.id = HomologousRecombinationSourceId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
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
    assembly: Union[Union[dict, AssemblyFragment], List[Union[dict, AssemblyFragment]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GibsonAssemblySourceId):
            self.id = GibsonAssemblySourceId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class InFusionSource(AssemblySource):
    """
    Represents the source of a sequence that is generated by In-Fusion cloning by Takara Bio
    """

    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SHAREYOURCLONING_LINKML["InFusionSource"]
    class_class_curie: ClassVar[str] = "shareyourcloning_linkml:InFusionSource"
    class_name: ClassVar[str] = "InFusionSource"
    class_model_uri: ClassVar[URIRef] = SHAREYOURCLONING_LINKML.InFusionSource

    id: Union[int, InFusionSourceId] = None
    assembly: Union[Union[dict, AssemblyFragment], List[Union[dict, AssemblyFragment]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, InFusionSourceId):
            self.id = InFusionSourceId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class OverlapExtensionPCRLigationSource(AssemblySource):
    """
    Represents the source of a sequence that is generated by ligation of PCR products as part of overlap extension
    PCR. Algorithmically equivalent to Gibson assembly.
    """

    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SHAREYOURCLONING_LINKML["OverlapExtensionPCRLigationSource"]
    class_class_curie: ClassVar[str] = "shareyourcloning_linkml:OverlapExtensionPCRLigationSource"
    class_name: ClassVar[str] = "OverlapExtensionPCRLigationSource"
    class_model_uri: ClassVar[URIRef] = SHAREYOURCLONING_LINKML.OverlapExtensionPCRLigationSource

    id: Union[int, OverlapExtensionPCRLigationSourceId] = None
    assembly: Union[Union[dict, AssemblyFragment], List[Union[dict, AssemblyFragment]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OverlapExtensionPCRLigationSourceId):
            self.id = OverlapExtensionPCRLigationSourceId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
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
    assembly: Union[Union[dict, AssemblyFragment], List[Union[dict, AssemblyFragment]]] = None
    restriction_enzymes: Union[str, List[str]] = None

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

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class GatewaySource(AssemblySource):
    """
    Represents the source of a sequence that is generated by Gateway cloning
    """

    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SHAREYOURCLONING_LINKML["GatewaySource"]
    class_class_curie: ClassVar[str] = "shareyourcloning_linkml:GatewaySource"
    class_name: ClassVar[str] = "GatewaySource"
    class_model_uri: ClassVar[URIRef] = SHAREYOURCLONING_LINKML.GatewaySource

    id: Union[int, GatewaySourceId] = None
    assembly: Union[Union[dict, AssemblyFragment], List[Union[dict, AssemblyFragment]]] = None
    reaction_type: Union[str, "GatewayReactionType"] = None
    greedy: Optional[Union[bool, Bool]] = False

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GatewaySourceId):
            self.id = GatewaySourceId(self.id)

        if self._is_empty(self.reaction_type):
            self.MissingRequiredField("reaction_type")
        if not isinstance(self.reaction_type, GatewayReactionType):
            self.reaction_type = GatewayReactionType(self.reaction_type)

        if self.greedy is not None and not isinstance(self.greedy, Bool):
            self.greedy = Bool(self.greedy)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
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
    assembly: Union[Union[dict, AssemblyFragment], List[Union[dict, AssemblyFragment]]] = None
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


@dataclass(repr=False)
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


@dataclass(repr=False)
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

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PolymeraseExtensionSourceId):
            self.id = PolymeraseExtensionSourceId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
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


@dataclass(repr=False)
class AnnotationReport(YAMLRoot):
    """
    Represents a report of an annotation step
    """

    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SHAREYOURCLONING_LINKML["AnnotationReport"]
    class_class_curie: ClassVar[str] = "shareyourcloning_linkml:AnnotationReport"
    class_name: ClassVar[str] = "AnnotationReport"
    class_model_uri: ClassVar[URIRef] = SHAREYOURCLONING_LINKML.AnnotationReport

    type: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
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


@dataclass(repr=False)
class PlannotateAnnotationReport(AnnotationReport):
    """
    Represents a report of an annotation step using Plannotate
    """

    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SHAREYOURCLONING_LINKML["PlannotateAnnotationReport"]
    class_class_curie: ClassVar[str] = "shareyourcloning_linkml:PlannotateAnnotationReport"
    class_name: ClassVar[str] = "PlannotateAnnotationReport"
    class_model_uri: ClassVar[URIRef] = SHAREYOURCLONING_LINKML.PlannotateAnnotationReport

    sseqid: Optional[str] = None
    start_location: Optional[int] = None
    end_location: Optional[int] = None
    strand: Optional[int] = None
    percent_identity: Optional[float] = None
    full_length_of_feature_in_db: Optional[int] = None
    length_of_found_feature: Optional[int] = None
    percent_match_length: Optional[float] = None
    fragment: Optional[Union[bool, Bool]] = None
    database: Optional[str] = None
    Feature: Optional[str] = None
    Type: Optional[str] = None
    Description: Optional[str] = None
    sequence: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.sseqid is not None and not isinstance(self.sseqid, str):
            self.sseqid = str(self.sseqid)

        if self.start_location is not None and not isinstance(self.start_location, int):
            self.start_location = int(self.start_location)

        if self.end_location is not None and not isinstance(self.end_location, int):
            self.end_location = int(self.end_location)

        if self.strand is not None and not isinstance(self.strand, int):
            self.strand = int(self.strand)

        if self.percent_identity is not None and not isinstance(self.percent_identity, float):
            self.percent_identity = float(self.percent_identity)

        if self.full_length_of_feature_in_db is not None and not isinstance(self.full_length_of_feature_in_db, int):
            self.full_length_of_feature_in_db = int(self.full_length_of_feature_in_db)

        if self.length_of_found_feature is not None and not isinstance(self.length_of_found_feature, int):
            self.length_of_found_feature = int(self.length_of_found_feature)

        if self.percent_match_length is not None and not isinstance(self.percent_match_length, float):
            self.percent_match_length = float(self.percent_match_length)

        if self.fragment is not None and not isinstance(self.fragment, Bool):
            self.fragment = Bool(self.fragment)

        if self.database is not None and not isinstance(self.database, str):
            self.database = str(self.database)

        if self.Feature is not None and not isinstance(self.Feature, str):
            self.Feature = str(self.Feature)

        if self.Type is not None and not isinstance(self.Type, str):
            self.Type = str(self.Type)

        if self.Description is not None and not isinstance(self.Description, str):
            self.Description = str(self.Description)

        if self.sequence is not None and not isinstance(self.sequence, str):
            self.sequence = str(self.sequence)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class AnnotationSource(Source):
    """
    Represents a computational step in which sequence features are annotated in a sequence
    """

    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SHAREYOURCLONING_LINKML["AnnotationSource"]
    class_class_curie: ClassVar[str] = "shareyourcloning_linkml:AnnotationSource"
    class_name: ClassVar[str] = "AnnotationSource"
    class_model_uri: ClassVar[URIRef] = SHAREYOURCLONING_LINKML.AnnotationSource

    id: Union[int, AnnotationSourceId] = None
    annotation_tool: Union[str, "AnnotationTool"] = None
    annotation_tool_version: Optional[str] = None
    annotation_report: Optional[Union[Union[dict, AnnotationReport], List[Union[dict, AnnotationReport]]]] = (
        empty_list()
    )

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AnnotationSourceId):
            self.id = AnnotationSourceId(self.id)

        if self._is_empty(self.annotation_tool):
            self.MissingRequiredField("annotation_tool")
        if not isinstance(self.annotation_tool, AnnotationTool):
            self.annotation_tool = AnnotationTool(self.annotation_tool)

        if self.annotation_tool_version is not None and not isinstance(self.annotation_tool_version, str):
            self.annotation_tool_version = str(self.annotation_tool_version)

        if not isinstance(self.annotation_report, list):
            self.annotation_report = [self.annotation_report] if self.annotation_report is not None else []
        self.annotation_report = [
            v if isinstance(v, AnnotationReport) else AnnotationReport(**as_dict(v)) for v in self.annotation_report
        ]

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


# Enumerations
class RepositoryName(EnumDefinitionImpl):

    addgene = PermissibleValue(text="addgene", description="Addgene")
    genbank = PermissibleValue(text="genbank", description="GenBank")
    benchling = PermissibleValue(text="benchling", description="Benchling")
    snapgene = PermissibleValue(text="snapgene", description="SnapGene plasmid library")
    euroscarf = PermissibleValue(text="euroscarf", description="Euroscarf (plasmids only)")
    igem = PermissibleValue(text="igem", description="iGEM collection")

    _defn = EnumDefinition(
        name="RepositoryName",
    )


class SequenceFileFormat(EnumDefinitionImpl):

    fasta = PermissibleValue(text="fasta")
    genbank = PermissibleValue(text="genbank")
    snapgene = PermissibleValue(text="snapgene")
    embl = PermissibleValue(text="embl")

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


class GatewayReactionType(EnumDefinitionImpl):

    LR = PermissibleValue(text="LR", description="LR reaction")
    BP = PermissibleValue(text="BP", description="BP reaction")

    _defn = EnumDefinition(
        name="GatewayReactionType",
    )


class AnnotationTool(EnumDefinitionImpl):

    plannotate = PermissibleValue(text="plannotate")

    _defn = EnumDefinition(
        name="AnnotationTool",
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

slots.output_name = Slot(
    uri=SHAREYOURCLONING_LINKML.output_name,
    name="output_name",
    curie=SHAREYOURCLONING_LINKML.curie("output_name"),
    model_uri=SHAREYOURCLONING_LINKML.output_name,
    domain=None,
    range=Optional[str],
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

slots.repository_id = Slot(
    uri=SHAREYOURCLONING_LINKML.repository_id,
    name="repository_id",
    curie=SHAREYOURCLONING_LINKML.curie("repository_id"),
    model_uri=SHAREYOURCLONING_LINKML.repository_id,
    domain=None,
    range=str,
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

slots.uploadedFileSource__circularize = Slot(
    uri=SHAREYOURCLONING_LINKML.circularize,
    name="uploadedFileSource__circularize",
    curie=SHAREYOURCLONING_LINKML.curie("circularize"),
    model_uri=SHAREYOURCLONING_LINKML.uploadedFileSource__circularize,
    domain=None,
    range=Optional[Union[bool, Bool]],
)

slots.repositoryIdSource__repository_name = Slot(
    uri=SHAREYOURCLONING_LINKML.repository_name,
    name="repositoryIdSource__repository_name",
    curie=SHAREYOURCLONING_LINKML.curie("repository_name"),
    model_uri=SHAREYOURCLONING_LINKML.repositoryIdSource__repository_name,
    domain=None,
    range=Union[str, "RepositoryName"],
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

slots.assemblyFragment__sequence = Slot(
    uri=SHAREYOURCLONING_LINKML.sequence,
    name="assemblyFragment__sequence",
    curie=SHAREYOURCLONING_LINKML.curie("sequence"),
    model_uri=SHAREYOURCLONING_LINKML.assemblyFragment__sequence,
    domain=None,
    range=Union[int, SequenceId],
)

slots.assemblyFragment__left_location = Slot(
    uri=SHAREYOURCLONING_LINKML.left_location,
    name="assemblyFragment__left_location",
    curie=SHAREYOURCLONING_LINKML.curie("left_location"),
    model_uri=SHAREYOURCLONING_LINKML.assemblyFragment__left_location,
    domain=None,
    range=Optional[Union[dict, SimpleSequenceLocation]],
)

slots.assemblyFragment__right_location = Slot(
    uri=SHAREYOURCLONING_LINKML.right_location,
    name="assemblyFragment__right_location",
    curie=SHAREYOURCLONING_LINKML.curie("right_location"),
    model_uri=SHAREYOURCLONING_LINKML.assemblyFragment__right_location,
    domain=None,
    range=Optional[Union[dict, SimpleSequenceLocation]],
)

slots.assemblyFragment__reverse_complemented = Slot(
    uri=SHAREYOURCLONING_LINKML.reverse_complemented,
    name="assemblyFragment__reverse_complemented",
    curie=SHAREYOURCLONING_LINKML.curie("reverse_complemented"),
    model_uri=SHAREYOURCLONING_LINKML.assemblyFragment__reverse_complemented,
    domain=None,
    range=Union[bool, Bool],
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
    range=Union[Union[dict, AssemblyFragment], List[Union[dict, AssemblyFragment]]],
)

slots.pCRSource__add_primer_features = Slot(
    uri=SHAREYOURCLONING_LINKML.add_primer_features,
    name="pCRSource__add_primer_features",
    curie=SHAREYOURCLONING_LINKML.curie("add_primer_features"),
    model_uri=SHAREYOURCLONING_LINKML.pCRSource__add_primer_features,
    domain=None,
    range=Optional[Union[bool, Bool]],
)

slots.gatewaySource__reaction_type = Slot(
    uri=SHAREYOURCLONING_LINKML.reaction_type,
    name="gatewaySource__reaction_type",
    curie=SHAREYOURCLONING_LINKML.curie("reaction_type"),
    model_uri=SHAREYOURCLONING_LINKML.gatewaySource__reaction_type,
    domain=None,
    range=Union[str, "GatewayReactionType"],
)

slots.gatewaySource__greedy = Slot(
    uri=SHAREYOURCLONING_LINKML.greedy,
    name="gatewaySource__greedy",
    curie=SHAREYOURCLONING_LINKML.curie("greedy"),
    model_uri=SHAREYOURCLONING_LINKML.gatewaySource__greedy,
    domain=None,
    range=Optional[Union[bool, Bool]],
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

slots.plannotateAnnotationReport__sseqid = Slot(
    uri=SHAREYOURCLONING_LINKML.sseqid,
    name="plannotateAnnotationReport__sseqid",
    curie=SHAREYOURCLONING_LINKML.curie("sseqid"),
    model_uri=SHAREYOURCLONING_LINKML.plannotateAnnotationReport__sseqid,
    domain=None,
    range=Optional[str],
)

slots.plannotateAnnotationReport__start_location = Slot(
    uri=SHAREYOURCLONING_LINKML.start_location,
    name="plannotateAnnotationReport__start_location",
    curie=SHAREYOURCLONING_LINKML.curie("start_location"),
    model_uri=SHAREYOURCLONING_LINKML.plannotateAnnotationReport__start_location,
    domain=None,
    range=Optional[int],
)

slots.plannotateAnnotationReport__end_location = Slot(
    uri=SHAREYOURCLONING_LINKML.end_location,
    name="plannotateAnnotationReport__end_location",
    curie=SHAREYOURCLONING_LINKML.curie("end_location"),
    model_uri=SHAREYOURCLONING_LINKML.plannotateAnnotationReport__end_location,
    domain=None,
    range=Optional[int],
)

slots.plannotateAnnotationReport__strand = Slot(
    uri=SHAREYOURCLONING_LINKML.strand,
    name="plannotateAnnotationReport__strand",
    curie=SHAREYOURCLONING_LINKML.curie("strand"),
    model_uri=SHAREYOURCLONING_LINKML.plannotateAnnotationReport__strand,
    domain=None,
    range=Optional[int],
)

slots.plannotateAnnotationReport__percent_identity = Slot(
    uri=SHAREYOURCLONING_LINKML.percent_identity,
    name="plannotateAnnotationReport__percent_identity",
    curie=SHAREYOURCLONING_LINKML.curie("percent_identity"),
    model_uri=SHAREYOURCLONING_LINKML.plannotateAnnotationReport__percent_identity,
    domain=None,
    range=Optional[float],
)

slots.plannotateAnnotationReport__full_length_of_feature_in_db = Slot(
    uri=SHAREYOURCLONING_LINKML.full_length_of_feature_in_db,
    name="plannotateAnnotationReport__full_length_of_feature_in_db",
    curie=SHAREYOURCLONING_LINKML.curie("full_length_of_feature_in_db"),
    model_uri=SHAREYOURCLONING_LINKML.plannotateAnnotationReport__full_length_of_feature_in_db,
    domain=None,
    range=Optional[int],
)

slots.plannotateAnnotationReport__length_of_found_feature = Slot(
    uri=SHAREYOURCLONING_LINKML.length_of_found_feature,
    name="plannotateAnnotationReport__length_of_found_feature",
    curie=SHAREYOURCLONING_LINKML.curie("length_of_found_feature"),
    model_uri=SHAREYOURCLONING_LINKML.plannotateAnnotationReport__length_of_found_feature,
    domain=None,
    range=Optional[int],
)

slots.plannotateAnnotationReport__percent_match_length = Slot(
    uri=SHAREYOURCLONING_LINKML.percent_match_length,
    name="plannotateAnnotationReport__percent_match_length",
    curie=SHAREYOURCLONING_LINKML.curie("percent_match_length"),
    model_uri=SHAREYOURCLONING_LINKML.plannotateAnnotationReport__percent_match_length,
    domain=None,
    range=Optional[float],
)

slots.plannotateAnnotationReport__fragment = Slot(
    uri=SHAREYOURCLONING_LINKML.fragment,
    name="plannotateAnnotationReport__fragment",
    curie=SHAREYOURCLONING_LINKML.curie("fragment"),
    model_uri=SHAREYOURCLONING_LINKML.plannotateAnnotationReport__fragment,
    domain=None,
    range=Optional[Union[bool, Bool]],
)

slots.plannotateAnnotationReport__database = Slot(
    uri=SHAREYOURCLONING_LINKML.database,
    name="plannotateAnnotationReport__database",
    curie=SHAREYOURCLONING_LINKML.curie("database"),
    model_uri=SHAREYOURCLONING_LINKML.plannotateAnnotationReport__database,
    domain=None,
    range=Optional[str],
)

slots.plannotateAnnotationReport__Feature = Slot(
    uri=SHAREYOURCLONING_LINKML.Feature,
    name="plannotateAnnotationReport__Feature",
    curie=SHAREYOURCLONING_LINKML.curie("Feature"),
    model_uri=SHAREYOURCLONING_LINKML.plannotateAnnotationReport__Feature,
    domain=None,
    range=Optional[str],
)

slots.plannotateAnnotationReport__Type = Slot(
    uri=SHAREYOURCLONING_LINKML.Type,
    name="plannotateAnnotationReport__Type",
    curie=SHAREYOURCLONING_LINKML.curie("Type"),
    model_uri=SHAREYOURCLONING_LINKML.plannotateAnnotationReport__Type,
    domain=None,
    range=Optional[str],
)

slots.plannotateAnnotationReport__Description = Slot(
    uri=SHAREYOURCLONING_LINKML.Description,
    name="plannotateAnnotationReport__Description",
    curie=SHAREYOURCLONING_LINKML.curie("Description"),
    model_uri=SHAREYOURCLONING_LINKML.plannotateAnnotationReport__Description,
    domain=None,
    range=Optional[str],
)

slots.plannotateAnnotationReport__sequence = Slot(
    uri=SHAREYOURCLONING_LINKML.sequence,
    name="plannotateAnnotationReport__sequence",
    curie=SHAREYOURCLONING_LINKML.curie("sequence"),
    model_uri=SHAREYOURCLONING_LINKML.plannotateAnnotationReport__sequence,
    domain=None,
    range=Optional[str],
)

slots.annotationSource__annotation_tool = Slot(
    uri=SHAREYOURCLONING_LINKML.annotation_tool,
    name="annotationSource__annotation_tool",
    curie=SHAREYOURCLONING_LINKML.curie("annotation_tool"),
    model_uri=SHAREYOURCLONING_LINKML.annotationSource__annotation_tool,
    domain=None,
    range=Union[str, "AnnotationTool"],
)

slots.annotationSource__annotation_tool_version = Slot(
    uri=SHAREYOURCLONING_LINKML.annotation_tool_version,
    name="annotationSource__annotation_tool_version",
    curie=SHAREYOURCLONING_LINKML.curie("annotation_tool_version"),
    model_uri=SHAREYOURCLONING_LINKML.annotationSource__annotation_tool_version,
    domain=None,
    range=Optional[str],
)

slots.annotationSource__annotation_report = Slot(
    uri=SHAREYOURCLONING_LINKML.annotation_report,
    name="annotationSource__annotation_report",
    curie=SHAREYOURCLONING_LINKML.curie("annotation_report"),
    model_uri=SHAREYOURCLONING_LINKML.annotationSource__annotation_report,
    domain=None,
    range=Optional[Union[Union[dict, AnnotationReport], List[Union[dict, AnnotationReport]]]],
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

slots.BenchlingUrlSource_repository_id = Slot(
    uri=SHAREYOURCLONING_LINKML.repository_id,
    name="BenchlingUrlSource_repository_id",
    curie=SHAREYOURCLONING_LINKML.curie("repository_id"),
    model_uri=SHAREYOURCLONING_LINKML.BenchlingUrlSource_repository_id,
    domain=BenchlingUrlSource,
    range=str,
    pattern=re.compile(r"^https:\/\/benchling\.com\/.+\.gb$"),
)

slots.SnapGenePlasmidSource_repository_id = Slot(
    uri=SHAREYOURCLONING_LINKML.repository_id,
    name="SnapGenePlasmidSource_repository_id",
    curie=SHAREYOURCLONING_LINKML.curie("repository_id"),
    model_uri=SHAREYOURCLONING_LINKML.SnapGenePlasmidSource_repository_id,
    domain=SnapGenePlasmidSource,
    range=str,
    pattern=re.compile(r"^.+\/.+$"),
)

slots.EuroscarfSource_repository_id = Slot(
    uri=SHAREYOURCLONING_LINKML.repository_id,
    name="EuroscarfSource_repository_id",
    curie=SHAREYOURCLONING_LINKML.curie("repository_id"),
    model_uri=SHAREYOURCLONING_LINKML.EuroscarfSource_repository_id,
    domain=EuroscarfSource,
    range=str,
    pattern=re.compile(r"^P\d+$"),
)

slots.IGEMSource_repository_id = Slot(
    uri=SHAREYOURCLONING_LINKML.repository_id,
    name="IGEMSource_repository_id",
    curie=SHAREYOURCLONING_LINKML.curie("repository_id"),
    model_uri=SHAREYOURCLONING_LINKML.IGEMSource_repository_id,
    domain=IGEMSource,
    range=str,
)

slots.IGEMSource_sequence_file_url = Slot(
    uri=SHAREYOURCLONING_LINKML.sequence_file_url,
    name="IGEMSource_sequence_file_url",
    curie=SHAREYOURCLONING_LINKML.curie("sequence_file_url"),
    model_uri=SHAREYOURCLONING_LINKML.IGEMSource_sequence_file_url,
    domain=IGEMSource,
    range=str,
    pattern=re.compile(
        r"^https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)$"
    ),
)

slots.RestrictionAndLigationSource_restriction_enzymes = Slot(
    uri=SHAREYOURCLONING_LINKML.restriction_enzymes,
    name="RestrictionAndLigationSource_restriction_enzymes",
    curie=SHAREYOURCLONING_LINKML.curie("restriction_enzymes"),
    model_uri=SHAREYOURCLONING_LINKML.RestrictionAndLigationSource_restriction_enzymes,
    domain=RestrictionAndLigationSource,
    range=Union[str, List[str]],
)
