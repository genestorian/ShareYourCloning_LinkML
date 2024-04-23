-- # Class: "NamedThing" Description: ""
--     * Slot: id Description: A unique identifier for a thing
-- # Class: "CloningStrategy" Description: "Represents a cloning strategy"
--     * Slot: id Description: 
--     * Slot: description Description: A description of the cloning strategy
-- # Class: "Sequence" Description: "Represents a sequence"
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: type Description: The type of the source
-- # Class: "TextFileSequence" Description: "A sequence (may have features) defined by the content of a text file"
--     * Slot: sequence_file_format Description: The format of a sequence file
--     * Slot: file_content Description: 
--     * Slot: overhang_crick_3prime Description: Taken from pydna's `dseq::ovhg`An integer describing the length of the crick strand overhang in the 5' of the molecule, or 3' of the crick strand
--     * Slot: overhang_watson_3prime Description: The equivalent of `overhang_crick_3prime` but for the watson strand
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: type Description: The type of the source
-- # Class: "Primer" Description: "An oligonucleotide or primer"
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: sequence Description: 
-- # Class: "SequenceCut" Description: "Represents a cut in a DNA sequence"
--     * Slot: cut_watson Description: The position of the cut in the watson strand. The cut is made before the base at this position (zero-based), so that cut position 1 cuts after the first base.
--     * Slot: overhang Description: The length of the overhang that is left after the cut. It can be negative, same meaning as in pydna's `dseq::ovhg` and biopython's `Bio.Restriction.RestrictionType.ovhg`.
--     * Slot: id Description: A unique identifier for a thing
-- # Class: "RestrictionSequenceCut" Description: "Represents a cut in a DNA sequence that is made by a restriction enzyme"
--     * Slot: restriction_enzyme Description: 
--     * Slot: cut_watson Description: The position of the cut in the watson strand. The cut is made before the base at this position (zero-based), so that cut position 1 cuts after the first base.
--     * Slot: overhang Description: The length of the overhang that is left after the cut. It can be negative, same meaning as in pydna's `dseq::ovhg` and biopython's `Bio.Restriction.RestrictionType.ovhg`.
--     * Slot: id Description: A unique identifier for a thing
-- # Class: "Source" Description: "Represents the source of a sequence"
--     * Slot: output Description: Identifier of the sequence that is the output of this source.
--     * Slot: type Description: The type of the source
--     * Slot: id Description: A unique identifier for a thing
-- # Class: "ManuallyTypedSource" Description: "Represents the source of a sequence that is manually typed by the user"
--     * Slot: user_input Description: 
--     * Slot: output Description: Identifier of the sequence that is the output of this source.
--     * Slot: type Description: The type of the source
--     * Slot: id Description: A unique identifier for a thing
-- # Class: "UploadedFileSource" Description: "Represents the source of a sequence that is uploaded as a file"
--     * Slot: sequence_file_format Description: The format of a sequence file
--     * Slot: file_name Description: The name of the file
--     * Slot: index_in_file Description: The index of the sequence in the file
--     * Slot: output Description: Identifier of the sequence that is the output of this source.
--     * Slot: type Description: The type of the source
--     * Slot: id Description: A unique identifier for a thing
-- # Class: "RepositoryIdSource" Description: "Represents the source of a sequence that is identified by a repository id"
--     * Slot: repository_name Description: 
--     * Slot: repository_id Description: The id of the sequence in the repository
--     * Slot: output Description: Identifier of the sequence that is the output of this source.
--     * Slot: type Description: The type of the source
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
--     * Slot: id Description: A unique identifier for a thing
-- # Class: "CutSource" Description: "Represents the source of a sequence that is a subfragment of another sequence, generated by sequence cutting."
--     * Slot: left_cut Description: 
--     * Slot: right_cut Description: 
--     * Slot: output Description: Identifier of the sequence that is the output of this source.
--     * Slot: type Description: The type of the source
--     * Slot: id Description: A unique identifier for a thing
-- # Class: "RestrictionCutSource" Description: "Represents the source of a sequence that is a subfragment of another sequence, generated by sequence cutting using restriction enzymes."
--     * Slot: left_cut Description: 
--     * Slot: right_cut Description: 
--     * Slot: output Description: Identifier of the sequence that is the output of this source.
--     * Slot: type Description: The type of the source
--     * Slot: id Description: A unique identifier for a thing
-- # Class: "CloningStrategy_sequences" Description: ""
--     * Slot: CloningStrategy_id Description: Autocreated FK slot
--     * Slot: sequences_id Description: The sequences that are used in the cloning strategy
-- # Class: "CloningStrategy_sources" Description: ""
--     * Slot: CloningStrategy_id Description: Autocreated FK slot
--     * Slot: sources_id Description: The sources of the sequences that are used in the cloning strategy
-- # Class: "CloningStrategy_primers" Description: ""
--     * Slot: CloningStrategy_id Description: Autocreated FK slot
--     * Slot: primers_id Description: The primers that are used in the cloning strategy
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
-- # Class: "CutSource_input" Description: ""
--     * Slot: CutSource_id Description: Autocreated FK slot
--     * Slot: input Description: Identifiers of the sequences that are an input to this source. If the source represents external import of a sequence, it's empty.
-- # Class: "RestrictionCutSource_input" Description: ""
--     * Slot: RestrictionCutSource_id Description: Autocreated FK slot
--     * Slot: input Description: Identifiers of the sequences that are an input to this source. If the source represents external import of a sequence, it's empty.

CREATE TABLE "NamedThing" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "CloningStrategy" (
	id INTEGER NOT NULL, 
	description TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Sequence" (
	id INTEGER NOT NULL, 
	type TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "TextFileSequence" (
	sequence_file_format VARCHAR(8) NOT NULL, 
	file_content TEXT, 
	overhang_crick_3prime INTEGER, 
	overhang_watson_3prime INTEGER, 
	id INTEGER NOT NULL, 
	type TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Primer" (
	id INTEGER NOT NULL, 
	name TEXT, 
	sequence TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "SequenceCut" (
	cut_watson INTEGER, 
	overhang INTEGER, 
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "RestrictionSequenceCut" (
	restriction_enzyme TEXT NOT NULL, 
	cut_watson INTEGER, 
	overhang INTEGER, 
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "Source" (
	output INTEGER, 
	type TEXT, 
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "ManuallyTypedSource" (
	user_input TEXT NOT NULL, 
	output INTEGER, 
	type TEXT, 
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "UploadedFileSource" (
	sequence_file_format VARCHAR(8) NOT NULL, 
	file_name TEXT, 
	index_in_file INTEGER, 
	output INTEGER, 
	type TEXT, 
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "RepositoryIdSource" (
	repository_name VARCHAR(7) NOT NULL, 
	repository_id TEXT NOT NULL, 
	output INTEGER, 
	type TEXT, 
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
	output INTEGER, 
	type TEXT, 
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "CutSource" (
	left_cut INTEGER, 
	right_cut INTEGER, 
	output INTEGER, 
	type TEXT, 
	id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(left_cut) REFERENCES "SequenceCut" (id), 
	FOREIGN KEY(right_cut) REFERENCES "SequenceCut" (id)
);
CREATE TABLE "RestrictionCutSource" (
	left_cut INTEGER, 
	right_cut INTEGER, 
	output INTEGER, 
	type TEXT, 
	id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(left_cut) REFERENCES "RestrictionSequenceCut" (id), 
	FOREIGN KEY(right_cut) REFERENCES "RestrictionSequenceCut" (id)
);
CREATE TABLE "CloningStrategy_sequences" (
	"CloningStrategy_id" INTEGER, 
	sequences_id INTEGER NOT NULL, 
	PRIMARY KEY ("CloningStrategy_id", sequences_id), 
	FOREIGN KEY("CloningStrategy_id") REFERENCES "CloningStrategy" (id), 
	FOREIGN KEY(sequences_id) REFERENCES "Sequence" (id)
);
CREATE TABLE "CloningStrategy_sources" (
	"CloningStrategy_id" INTEGER, 
	sources_id INTEGER NOT NULL, 
	PRIMARY KEY ("CloningStrategy_id", sources_id), 
	FOREIGN KEY("CloningStrategy_id") REFERENCES "CloningStrategy" (id), 
	FOREIGN KEY(sources_id) REFERENCES "Source" (id)
);
CREATE TABLE "CloningStrategy_primers" (
	"CloningStrategy_id" INTEGER, 
	primers_id INTEGER, 
	PRIMARY KEY ("CloningStrategy_id", primers_id), 
	FOREIGN KEY("CloningStrategy_id") REFERENCES "CloningStrategy" (id), 
	FOREIGN KEY(primers_id) REFERENCES "Primer" (id)
);
CREATE TABLE "Source_input" (
	"Source_id" INTEGER, 
	input INTEGER, 
	PRIMARY KEY ("Source_id", input), 
	FOREIGN KEY("Source_id") REFERENCES "Source" (id)
);
CREATE TABLE "ManuallyTypedSource_input" (
	"ManuallyTypedSource_id" INTEGER, 
	input INTEGER, 
	PRIMARY KEY ("ManuallyTypedSource_id", input), 
	FOREIGN KEY("ManuallyTypedSource_id") REFERENCES "ManuallyTypedSource" (id)
);
CREATE TABLE "UploadedFileSource_input" (
	"UploadedFileSource_id" INTEGER, 
	input INTEGER, 
	PRIMARY KEY ("UploadedFileSource_id", input), 
	FOREIGN KEY("UploadedFileSource_id") REFERENCES "UploadedFileSource" (id)
);
CREATE TABLE "RepositoryIdSource_input" (
	"RepositoryIdSource_id" INTEGER, 
	input INTEGER, 
	PRIMARY KEY ("RepositoryIdSource_id", input), 
	FOREIGN KEY("RepositoryIdSource_id") REFERENCES "RepositoryIdSource" (id)
);
CREATE TABLE "GenomeCoordinatesSource_input" (
	"GenomeCoordinatesSource_id" INTEGER, 
	input INTEGER, 
	PRIMARY KEY ("GenomeCoordinatesSource_id", input), 
	FOREIGN KEY("GenomeCoordinatesSource_id") REFERENCES "GenomeCoordinatesSource" (id)
);
CREATE TABLE "CutSource_input" (
	"CutSource_id" INTEGER, 
	input INTEGER, 
	PRIMARY KEY ("CutSource_id", input), 
	FOREIGN KEY("CutSource_id") REFERENCES "CutSource" (id)
);
CREATE TABLE "RestrictionCutSource_input" (
	"RestrictionCutSource_id" INTEGER, 
	input INTEGER, 
	PRIMARY KEY ("RestrictionCutSource_id", input), 
	FOREIGN KEY("RestrictionCutSource_id") REFERENCES "RestrictionCutSource" (id)
);