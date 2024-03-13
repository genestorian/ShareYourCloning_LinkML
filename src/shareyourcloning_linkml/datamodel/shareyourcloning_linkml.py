# Auto generated from shareyourcloning_linkml.yaml by pythongen.py version: 0.0.1
# Generation date: 2024-03-13T18:09:20
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
    input: Union[int, List[int]] = None
    output: int = None
    type: Union[str, "SourceType"] = None
    kind: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.input):
            self.MissingRequiredField("input")
        if not isinstance(self.input, list):
            self.input = [self.input] if self.input is not None else []
        self.input = [v if isinstance(v, int) else int(v) for v in self.input]

        if self._is_empty(self.output):
            self.MissingRequiredField("output")
        if not isinstance(self.output, int):
            self.output = int(self.output)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, SourceType):
            self.type = SourceType(self.type)

        if self._is_empty(self.kind):
            self.MissingRequiredField("kind")
        if not isinstance(self.kind, str):
            self.kind = str(self.kind)

        super().__post_init__(**kwargs)


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
    input: Union[int, List[int]] = None
    output: int = None
    kind: str = None
    type: Union[str, "SourceType"] = None
    user_input: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ManuallyTypedSourceId):
            self.id = ManuallyTypedSourceId(self.id)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, SourceType):
            self.type = SourceType(self.type)

        if self.user_input is not None and not isinstance(self.user_input, str):
            self.user_input = str(self.user_input)

        super().__post_init__(**kwargs)


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
    input: Union[int, List[int]] = None
    output: int = None
    kind: str = None
    type: Union[str, "SourceType"] = None
    file_name: Optional[str] = None
    index_in_file: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, UploadedFileSourceId):
            self.id = UploadedFileSourceId(self.id)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, SourceType):
            self.type = SourceType(self.type)

        if self.file_name is not None and not isinstance(self.file_name, str):
            self.file_name = str(self.file_name)

        if self.index_in_file is not None and not isinstance(self.index_in_file, int):
            self.index_in_file = int(self.index_in_file)

        super().__post_init__(**kwargs)


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
    input: Union[int, List[int]] = None
    output: int = None
    kind: str = None
    repository_name: Union[str, "RepositoryName"] = None
    repository_id: str = None
    type: Union[str, "SourceType"] = None

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

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, SourceType):
            self.type = SourceType(self.type)

        super().__post_init__(**kwargs)


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
    input: Union[int, List[int]] = None
    output: int = None
    kind: str = None
    sequence_accession: str = None
    start: int = None
    stop: int = None
    strand: int = None
    type: Union[str, "SourceType"] = None
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

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, SourceType):
            self.type = SourceType(self.type)

        if self.assembly_accession is not None and not isinstance(self.assembly_accession, str):
            self.assembly_accession = str(self.assembly_accession)

        if self.locus_tag is not None and not isinstance(self.locus_tag, str):
            self.locus_tag = str(self.locus_tag)

        if self.gene_id is not None and not isinstance(self.gene_id, int):
            self.gene_id = int(self.gene_id)

        super().__post_init__(**kwargs)


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

class SourceType(EnumDefinitionImpl):

    repository_id = PermissibleValue(text="repository_id")
    file = PermissibleValue(text="file")
    restriction = PermissibleValue(text="restriction")
    ligation = PermissibleValue(text="ligation")
    PCR = PermissibleValue(text="PCR")
    homologous_recombination = PermissibleValue(text="homologous_recombination")
    gibson_assembly = PermissibleValue(text="gibson_assembly")
    restriction_and_ligation = PermissibleValue(text="restriction_and_ligation")
    genome_coordinates = PermissibleValue(text="genome_coordinates")
    manually_typed = PermissibleValue(text="manually_typed")

    _defn = EnumDefinition(
        name="SourceType",
    )

# Slots
class slots:
    pass

slots.id = Slot(uri=SCHEMA.identifier, name="id", curie=SCHEMA.curie('identifier'),
                   model_uri=SHAREYOURCLONING_LINKML.id, domain=None, range=URIRef)

slots.restriction_enzyme = Slot(uri=SHAREYOURCLONING_LINKML.restriction_enzyme, name="restriction_enzyme", curie=SHAREYOURCLONING_LINKML.curie('restriction_enzyme'),
                   model_uri=SHAREYOURCLONING_LINKML.restriction_enzyme, domain=None, range=Optional[str])

slots.input = Slot(uri=SHAREYOURCLONING_LINKML.input, name="input", curie=SHAREYOURCLONING_LINKML.curie('input'),
                   model_uri=SHAREYOURCLONING_LINKML.input, domain=None, range=Union[int, List[int]])

slots.output = Slot(uri=SHAREYOURCLONING_LINKML.output, name="output", curie=SHAREYOURCLONING_LINKML.curie('output'),
                   model_uri=SHAREYOURCLONING_LINKML.output, domain=None, range=int)

slots.type = Slot(uri=SHAREYOURCLONING_LINKML.type, name="type", curie=SHAREYOURCLONING_LINKML.curie('type'),
                   model_uri=SHAREYOURCLONING_LINKML.type, domain=None, range=Union[str, "SourceType"])

slots.source__kind = Slot(uri=SHAREYOURCLONING_LINKML.kind, name="source__kind", curie=SHAREYOURCLONING_LINKML.curie('kind'),
                   model_uri=SHAREYOURCLONING_LINKML.source__kind, domain=None, range=str)

slots.manuallyTypedSource__user_input = Slot(uri=SHAREYOURCLONING_LINKML.user_input, name="manuallyTypedSource__user_input", curie=SHAREYOURCLONING_LINKML.curie('user_input'),
                   model_uri=SHAREYOURCLONING_LINKML.manuallyTypedSource__user_input, domain=None, range=Optional[str],
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

slots.ManuallyTypedSource_type = Slot(uri=SHAREYOURCLONING_LINKML.type, name="ManuallyTypedSource_type", curie=SHAREYOURCLONING_LINKML.curie('type'),
                   model_uri=SHAREYOURCLONING_LINKML.ManuallyTypedSource_type, domain=ManuallyTypedSource, range=Union[str, "SourceType"])

slots.UploadedFileSource_type = Slot(uri=SHAREYOURCLONING_LINKML.type, name="UploadedFileSource_type", curie=SHAREYOURCLONING_LINKML.curie('type'),
                   model_uri=SHAREYOURCLONING_LINKML.UploadedFileSource_type, domain=UploadedFileSource, range=Union[str, "SourceType"])

slots.RepositoryIdSource_type = Slot(uri=SHAREYOURCLONING_LINKML.type, name="RepositoryIdSource_type", curie=SHAREYOURCLONING_LINKML.curie('type'),
                   model_uri=SHAREYOURCLONING_LINKML.RepositoryIdSource_type, domain=RepositoryIdSource, range=Union[str, "SourceType"])

slots.GenomeCoordinatesSource_type = Slot(uri=SHAREYOURCLONING_LINKML.type, name="GenomeCoordinatesSource_type", curie=SHAREYOURCLONING_LINKML.curie('type'),
                   model_uri=SHAREYOURCLONING_LINKML.GenomeCoordinatesSource_type, domain=GenomeCoordinatesSource, range=Union[str, "SourceType"])