-- # Class: "NamedThing" Description: ""
--     * Slot: id Description: A unique identifier for a thing
-- # Class: "Source" Description: "Represents the source of a sequence"
--     * Slot: output Description: Identifier of the sequence that is the output of this source.
--     * Slot: type Description: The type of the source
--     * Slot: kind Description: The kind entity (always equal to "source"). Should probably be removed.
--     * Slot: id Description: A unique identifier for a thing
-- # Class: "ManuallyTypedSource" Description: "Represents the source of a sequence that is manually typed by the user"
--     * Slot: user_input Description: 
--     * Slot: output Description: Identifier of the sequence that is the output of this source.
--     * Slot: type Description: The type of the source
--     * Slot: kind Description: The kind entity (always equal to "source"). Should probably be removed.
--     * Slot: id Description: A unique identifier for a thing
-- # Class: "UploadedFileSource" Description: "Represents the source of a sequence that is uploaded as a file"
--     * Slot: file_name Description: The name of the file
--     * Slot: index_in_file Description: The index of the sequence in the file
--     * Slot: output Description: Identifier of the sequence that is the output of this source.
--     * Slot: type Description: The type of the source
--     * Slot: kind Description: The kind entity (always equal to "source"). Should probably be removed.
--     * Slot: id Description: A unique identifier for a thing
-- # Class: "RepositoryIdSource" Description: "Represents the source of a sequence that is identified by a repository id"
--     * Slot: repository_name Description: 
--     * Slot: repository_id Description: The id of the sequence in the repository
--     * Slot: output Description: Identifier of the sequence that is the output of this source.
--     * Slot: type Description: The type of the source
--     * Slot: kind Description: The kind entity (always equal to "source"). Should probably be removed.
--     * Slot: id Description: A unique identifier for a thing
-- # Class: "GenomeCoordinatesSource" Description: "Represents the source of a sequence that is identified by genome coordinates, requested from NCBI"
--     * Slot: assembly_accession Description: The accession of the assembly
--     * Slot: sequence_accession Description: The accession of the sequence
--     * Slot: locus_tag Description: The locus tag of the sequence
--     * Slot: gene_id Description: The gene id of the sequence
--     * Slot: start Description: The starting coordinate (1-based) of the sequence in the sequence accession
--     * Slot: stop Description: The ending coordinate (1-based) of the sequence in the sequence accession
--     * Slot: strand Description: The strand of the sequence in the sequence accession, should be 1 or -1
--     * Slot: output Description: Identifier of the sequence that is the output of this source.
--     * Slot: type Description: The type of the source
--     * Slot: kind Description: The kind entity (always equal to "source"). Should probably be removed.
--     * Slot: id Description: A unique identifier for a thing
-- # Class: "Source_input" Description: ""
--     * Slot: Source_id Description: Autocreated FK slot
--     * Slot: input Description: Identifiers of the sequences that are an input to this source. If the source represents external import of a sequence, it's empty.
-- # Class: "ManuallyTypedSource_input" Description: ""
--     * Slot: ManuallyTypedSource_id Description: Autocreated FK slot
--     * Slot: input Description: Identifiers of the sequences that are an input to this source. If the source represents external import of a sequence, it's empty.
-- # Class: "UploadedFileSource_input" Description: ""
--     * Slot: UploadedFileSource_id Description: Autocreated FK slot
--     * Slot: input Description: Identifiers of the sequences that are an input to this source. If the source represents external import of a sequence, it's empty.
-- # Class: "RepositoryIdSource_input" Description: ""
--     * Slot: RepositoryIdSource_id Description: Autocreated FK slot
--     * Slot: input Description: Identifiers of the sequences that are an input to this source. If the source represents external import of a sequence, it's empty.
-- # Class: "GenomeCoordinatesSource_input" Description: ""
--     * Slot: GenomeCoordinatesSource_id Description: Autocreated FK slot
--     * Slot: input Description: Identifiers of the sequences that are an input to this source. If the source represents external import of a sequence, it's empty.

CREATE TABLE "NamedThing" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "Source" (
	output INTEGER NOT NULL, 
	type VARCHAR(24) NOT NULL, 
	kind TEXT NOT NULL, 
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "ManuallyTypedSource" (
	user_input TEXT, 
	output INTEGER NOT NULL, 
	type VARCHAR(24) NOT NULL, 
	kind TEXT NOT NULL, 
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "UploadedFileSource" (
	file_name TEXT, 
	index_in_file INTEGER, 
	output INTEGER NOT NULL, 
	type VARCHAR(24) NOT NULL, 
	kind TEXT NOT NULL, 
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "RepositoryIdSource" (
	repository_name VARCHAR(7) NOT NULL, 
	repository_id TEXT NOT NULL, 
	output INTEGER NOT NULL, 
	type VARCHAR(24) NOT NULL, 
	kind TEXT NOT NULL, 
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "GenomeCoordinatesSource" (
	assembly_accession TEXT, 
	sequence_accession TEXT NOT NULL, 
	locus_tag TEXT, 
	gene_id INTEGER, 
	start INTEGER NOT NULL, 
	stop INTEGER NOT NULL, 
	strand INTEGER NOT NULL, 
	output INTEGER NOT NULL, 
	type VARCHAR(24) NOT NULL, 
	kind TEXT NOT NULL, 
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "Source_input" (
	"Source_id" INTEGER, 
	input INTEGER NOT NULL, 
	PRIMARY KEY ("Source_id", input), 
	FOREIGN KEY("Source_id") REFERENCES "Source" (id)
);
CREATE TABLE "ManuallyTypedSource_input" (
	"ManuallyTypedSource_id" INTEGER, 
	input INTEGER NOT NULL, 
	PRIMARY KEY ("ManuallyTypedSource_id", input), 
	FOREIGN KEY("ManuallyTypedSource_id") REFERENCES "ManuallyTypedSource" (id)
);
CREATE TABLE "UploadedFileSource_input" (
	"UploadedFileSource_id" INTEGER, 
	input INTEGER NOT NULL, 
	PRIMARY KEY ("UploadedFileSource_id", input), 
	FOREIGN KEY("UploadedFileSource_id") REFERENCES "UploadedFileSource" (id)
);
CREATE TABLE "RepositoryIdSource_input" (
	"RepositoryIdSource_id" INTEGER, 
	input INTEGER NOT NULL, 
	PRIMARY KEY ("RepositoryIdSource_id", input), 
	FOREIGN KEY("RepositoryIdSource_id") REFERENCES "RepositoryIdSource" (id)
);
CREATE TABLE "GenomeCoordinatesSource_input" (
	"GenomeCoordinatesSource_id" INTEGER, 
	input INTEGER NOT NULL, 
	PRIMARY KEY ("GenomeCoordinatesSource_id", input), 
	FOREIGN KEY("GenomeCoordinatesSource_id") REFERENCES "GenomeCoordinatesSource" (id)
);