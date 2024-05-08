-- # Class: "NamedThing" Description: ""
--     * Slot: id Description: A unique identifier for a thing
-- # Class: "Sequence" Description: "Represents a sequence"
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: type Description: The type of the source
--     * Slot: CloningStrategy_id Description: Autocreated FK slot
-- # Class: "TextFileSequence" Description: "A sequence (may have features) defined by the content of a text file"
--     * Slot: sequence_file_format Description: The format of a sequence file
--     * Slot: overhang_crick_3prime Description: Taken from pydna's `dseq::ovhg`An integer describing the length of the crick strand overhang in the 5' of the molecule, or 3' of the crick strand
--     * Slot: overhang_watson_3prime Description: The equivalent of `overhang_crick_3prime` but for the watson strand
--     * Slot: file_content Description:
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: type Description: The type of the source
-- # Class: "Primer" Description: "An oligonucleotide or primer"
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: sequence Description:
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: type Description: The type of the source
--     * Slot: CloningStrategy_id Description: Autocreated FK slot
-- # Class: "SequenceCut" Description: "Represents a cut in a DNA sequence"
--     * Slot: id Description:
--     * Slot: cut_watson Description: The position of the cut in the watson strand. The cut is made before the base at this position (zero-based), so that cut position 1 cuts after the first base.
--     * Slot: overhang Description: The length of the overhang that is left after the cut. It can be negative, same meaning as in pydna's `dseq::ovhg` and biopython's `Bio.Restriction.RestrictionType.ovhg`.
-- # Class: "RestrictionSequenceCut" Description: "Represents a cut in a DNA sequence that is made by a restriction enzyme"
--     * Slot: id Description:
--     * Slot: restriction_enzyme Description:
--     * Slot: cut_watson Description: The position of the cut in the watson strand. The cut is made before the base at this position (zero-based), so that cut position 1 cuts after the first base.
--     * Slot: overhang Description: The length of the overhang that is left after the cut. It can be negative, same meaning as in pydna's `dseq::ovhg` and biopython's `Bio.Restriction.RestrictionType.ovhg`.
-- # Class: "Source" Description: "Represents the source of a sequence"
--     * Slot: output Description: Identifier of the sequence that is the output of this source.
--     * Slot: type Description: The type of the source
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: CloningStrategy_id Description: Autocreated FK slot
-- # Class: "ManuallyTypedSource" Description: "Represents the source of a sequence that is manually typed by the user"
--     * Slot: overhang_crick_3prime Description: Taken from pydna's `dseq::ovhg`An integer describing the length of the crick strand overhang in the 5' of the molecule, or 3' of the crick strand
--     * Slot: overhang_watson_3prime Description: The equivalent of `overhang_crick_3prime` but for the watson strand
--     * Slot: user_input Description:
--     * Slot: circular Description: Whether the sequence is circular or not
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
-- # Class: "AddGeneIdSource" Description: "Represents the source of a sequence that is identified by an AddGene id"
--     * Slot: sequence_file_url Description: The URL of a sequence file
--     * Slot: addgene_sequence_type Description:
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
--     * Slot: end Description: The ending coordinate (1-based) of the sequence in the sequence accession
--     * Slot: strand Description: The strand of the sequence in the sequence accession, should be 1 or -1
--     * Slot: output Description: Identifier of the sequence that is the output of this source.
--     * Slot: type Description: The type of the source
--     * Slot: id Description: A unique identifier for a thing
-- # Class: "SequenceCutSource" Description: "Represents the source of a sequence that is a subfragment of another sequence, generated by sequence cutting."
--     * Slot: output Description: Identifier of the sequence that is the output of this source.
--     * Slot: type Description: The type of the source
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: left_edge_id Description:
--     * Slot: right_edge_id Description:
-- # Class: "RestrictionEnzymeDigestionSource" Description: "Represents the source of a sequence that is a subfragment of another sequence, generated by sequence cutting using restriction enzymes."
--     * Slot: output Description: Identifier of the sequence that is the output of this source.
--     * Slot: type Description: The type of the source
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: left_edge_id Description:
--     * Slot: right_edge_id Description:
-- # Class: "SimpleSequenceLocation" Description: "Represents a location within a sequence, for now support for ranges only"
--     * Slot: id Description:
--     * Slot: start Description: The starting coordinate (1-based) of the location
--     * Slot: end Description: The ending coordinate (1-based) of the location
--     * Slot: strand Description: The strand of the location, should be 1 or -1 or null
-- # Class: "AssemblyJoinComponent" Description: "Represents a component of a join between two fragments in an assembly"
--     * Slot: id Description:
--     * Slot: sequence Description:
--     * Slot: reverse_complemented Description: Whether the sequence is reverse complemented in the join
--     * Slot: location_id Description: Location of the overlap in the fragment. Might be an empty location (start == end) to indicate blunt join.
-- # Class: "AssemblyJoin" Description: "Represents a joint between two fragments in an assembly"
--     * Slot: id Description:
--     * Slot: AssemblySource_id Description: Autocreated FK slot
--     * Slot: PCRSource_id Description: Autocreated FK slot
--     * Slot: LigationSource_id Description: Autocreated FK slot
--     * Slot: HomologousRecombinationSource_id Description: Autocreated FK slot
--     * Slot: GibsonAssemblySource_id Description: Autocreated FK slot
--     * Slot: RestrictionAndLigationSource_id Description: Autocreated FK slot
--     * Slot: CRISPRSource_id Description: Autocreated FK slot
--     * Slot: left_id Description:
--     * Slot: right_id Description:
-- # Class: "AssemblySource" Description: "Represents the source of a sequence that is an assembly of other sequences"
--     * Slot: circular Description: Whether the assembly is circular or not
--     * Slot: output Description: Identifier of the sequence that is the output of this source.
--     * Slot: type Description: The type of the source
--     * Slot: id Description: A unique identifier for a thing
-- # Class: "PCRSource" Description: "Represents the source of a sequence that is generated by PCR"
--     * Slot: forward_primer Description: The forward primer used in the PCR
--     * Slot: reverse_primer Description: The reverse primer used in the PCR
--     * Slot: circular Description: Whether the assembly is circular or not
--     * Slot: output Description: Identifier of the sequence that is the output of this source.
--     * Slot: type Description: The type of the source
--     * Slot: id Description: A unique identifier for a thing
-- # Class: "LigationSource" Description: "Represents the source of a sequence that is generated by ligation with sticky or blunt ends."
--     * Slot: circular Description: Whether the assembly is circular or not
--     * Slot: output Description: Identifier of the sequence that is the output of this source.
--     * Slot: type Description: The type of the source
--     * Slot: id Description: A unique identifier for a thing
-- # Class: "HomologousRecombinationSource" Description: "Represents the source of a sequence that is generated by homologous recombination"
--     * Slot: circular Description: Whether the assembly is circular or not
--     * Slot: output Description: Identifier of the sequence that is the output of this source.
--     * Slot: type Description: The type of the source
--     * Slot: id Description: A unique identifier for a thing
-- # Class: "GibsonAssemblySource" Description: "Represents the source of a sequence that is generated by Gibson assembly"
--     * Slot: circular Description: Whether the assembly is circular or not
--     * Slot: output Description: Identifier of the sequence that is the output of this source.
--     * Slot: type Description: The type of the source
--     * Slot: id Description: A unique identifier for a thing
-- # Class: "RestrictionAndLigationSource" Description: "Represents the source of a sequence that is generated by restriction and ligation"
--     * Slot: circular Description: Whether the assembly is circular or not
--     * Slot: output Description: Identifier of the sequence that is the output of this source.
--     * Slot: type Description: The type of the source
--     * Slot: id Description: A unique identifier for a thing
-- # Class: "CRISPRSource" Description: "Represents the source of a sequence that is generated by CRISPR"
--     * Slot: circular Description: Whether the assembly is circular or not
--     * Slot: output Description: Identifier of the sequence that is the output of this source.
--     * Slot: type Description: The type of the source
--     * Slot: id Description: A unique identifier for a thing
-- # Class: "OligoHybridizationSource" Description: "Represents the source of a sequence that is generated by oligo hybridization"
--     * Slot: overhang_crick_3prime Description: Taken from pydna's `dseq::ovhg`An integer describing the length of the crick strand overhang in the 5' of the molecule, or 3' of the crick strand
--     * Slot: forward_oligo Description: The forward oligo used in the hybridization
--     * Slot: reverse_oligo Description: The reverse oligo used in the hybridization
--     * Slot: output Description: Identifier of the sequence that is the output of this source.
--     * Slot: type Description: The type of the source
--     * Slot: id Description: A unique identifier for a thing
-- # Class: "PolymeraseExtensionSource" Description: "Represents the source of a sequence that is generated by polymerase extension"
--     * Slot: output Description: Identifier of the sequence that is the output of this source.
--     * Slot: type Description: The type of the source
--     * Slot: id Description: A unique identifier for a thing
-- # Class: "CloningStrategy" Description: "Represents a cloning strategy"
--     * Slot: id Description:
--     * Slot: description Description: A description of the cloning strategy
-- # Class: "Source_input" Description: ""
--     * Slot: Source_id Description: Autocreated FK slot
--     * Slot: input_id Description: The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.
-- # Class: "ManuallyTypedSource_input" Description: ""
--     * Slot: ManuallyTypedSource_id Description: Autocreated FK slot
--     * Slot: input_id Description: The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.
-- # Class: "UploadedFileSource_input" Description: ""
--     * Slot: UploadedFileSource_id Description: Autocreated FK slot
--     * Slot: input_id Description: The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.
-- # Class: "RepositoryIdSource_input" Description: ""
--     * Slot: RepositoryIdSource_id Description: Autocreated FK slot
--     * Slot: input_id Description: The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.
-- # Class: "AddGeneIdSource_input" Description: ""
--     * Slot: AddGeneIdSource_id Description: Autocreated FK slot
--     * Slot: input_id Description: The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.
-- # Class: "GenomeCoordinatesSource_input" Description: ""
--     * Slot: GenomeCoordinatesSource_id Description: Autocreated FK slot
--     * Slot: input_id Description: The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.
-- # Class: "SequenceCutSource_input" Description: ""
--     * Slot: SequenceCutSource_id Description: Autocreated FK slot
--     * Slot: input_id Description: The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.
-- # Class: "RestrictionEnzymeDigestionSource_input" Description: ""
--     * Slot: RestrictionEnzymeDigestionSource_id Description: Autocreated FK slot
--     * Slot: input_id Description: The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.
-- # Class: "AssemblySource_input" Description: ""
--     * Slot: AssemblySource_id Description: Autocreated FK slot
--     * Slot: input_id Description: The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.
-- # Class: "PCRSource_input" Description: ""
--     * Slot: PCRSource_id Description: Autocreated FK slot
--     * Slot: input_id Description: The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.
-- # Class: "LigationSource_input" Description: ""
--     * Slot: LigationSource_id Description: Autocreated FK slot
--     * Slot: input_id Description: The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.
-- # Class: "HomologousRecombinationSource_input" Description: ""
--     * Slot: HomologousRecombinationSource_id Description: Autocreated FK slot
--     * Slot: input_id Description: The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.
-- # Class: "GibsonAssemblySource_input" Description: ""
--     * Slot: GibsonAssemblySource_id Description: Autocreated FK slot
--     * Slot: input_id Description: The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.
-- # Class: "RestrictionAndLigationSource_restriction_enzymes" Description: ""
--     * Slot: RestrictionAndLigationSource_id Description: Autocreated FK slot
--     * Slot: restriction_enzymes Description:
-- # Class: "RestrictionAndLigationSource_input" Description: ""
--     * Slot: RestrictionAndLigationSource_id Description: Autocreated FK slot
--     * Slot: input_id Description: The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.
-- # Class: "CRISPRSource_guides" Description: ""
--     * Slot: CRISPRSource_id Description: Autocreated FK slot
--     * Slot: guides_id Description: The guide RNAs used in the CRISPR
-- # Class: "CRISPRSource_input" Description: ""
--     * Slot: CRISPRSource_id Description: Autocreated FK slot
--     * Slot: input_id Description: The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.
-- # Class: "OligoHybridizationSource_input" Description: ""
--     * Slot: OligoHybridizationSource_id Description: Autocreated FK slot
--     * Slot: input_id Description: The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.
-- # Class: "PolymeraseExtensionSource_input" Description: ""
--     * Slot: PolymeraseExtensionSource_id Description: Autocreated FK slot
--     * Slot: input_id Description: The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.

CREATE TABLE "NamedThing" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE TABLE "TextFileSequence" (
	sequence_file_format VARCHAR(8) NOT NULL,
	overhang_crick_3prime INTEGER,
	overhang_watson_3prime INTEGER,
	file_content TEXT,
	id INTEGER NOT NULL,
	type TEXT,
	PRIMARY KEY (id)
);
CREATE TABLE "SequenceCut" (
	id INTEGER NOT NULL,
	cut_watson INTEGER NOT NULL,
	overhang INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE TABLE "RestrictionSequenceCut" (
	id INTEGER NOT NULL,
	restriction_enzyme TEXT NOT NULL,
	cut_watson INTEGER NOT NULL,
	overhang INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE TABLE "SimpleSequenceLocation" (
	id INTEGER NOT NULL,
	start INTEGER NOT NULL,
	"end" INTEGER NOT NULL,
	strand INTEGER,
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
	"CloningStrategy_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("CloningStrategy_id") REFERENCES "CloningStrategy" (id)
);
CREATE TABLE "Primer" (
	name TEXT,
	sequence TEXT,
	id INTEGER NOT NULL,
	type TEXT,
	"CloningStrategy_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("CloningStrategy_id") REFERENCES "CloningStrategy" (id)
);
CREATE TABLE "Source" (
	output INTEGER,
	type TEXT,
	id INTEGER NOT NULL,
	"CloningStrategy_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(output) REFERENCES "Sequence" (id),
	FOREIGN KEY("CloningStrategy_id") REFERENCES "CloningStrategy" (id)
);
CREATE TABLE "ManuallyTypedSource" (
	overhang_crick_3prime INTEGER,
	overhang_watson_3prime INTEGER,
	user_input TEXT NOT NULL,
	circular BOOLEAN,
	output INTEGER,
	type TEXT,
	id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(output) REFERENCES "Sequence" (id)
);
CREATE TABLE "UploadedFileSource" (
	sequence_file_format VARCHAR(8) NOT NULL,
	file_name TEXT,
	index_in_file INTEGER,
	output INTEGER,
	type TEXT,
	id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(output) REFERENCES "Sequence" (id)
);
CREATE TABLE "RepositoryIdSource" (
	repository_name VARCHAR(7) NOT NULL,
	repository_id TEXT NOT NULL,
	output INTEGER,
	type TEXT,
	id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(output) REFERENCES "Sequence" (id)
);
CREATE TABLE "AddGeneIdSource" (
	sequence_file_url TEXT,
	addgene_sequence_type VARCHAR(14),
	repository_name VARCHAR(7) NOT NULL,
	repository_id TEXT NOT NULL,
	output INTEGER,
	type TEXT,
	id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(output) REFERENCES "Sequence" (id)
);
CREATE TABLE "GenomeCoordinatesSource" (
	assembly_accession TEXT,
	sequence_accession TEXT NOT NULL,
	locus_tag TEXT,
	gene_id INTEGER,
	start INTEGER NOT NULL,
	"end" INTEGER NOT NULL,
	strand INTEGER NOT NULL,
	output INTEGER,
	type TEXT,
	id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(output) REFERENCES "Sequence" (id)
);
CREATE TABLE "SequenceCutSource" (
	output INTEGER,
	type TEXT,
	id INTEGER NOT NULL,
	left_edge_id INTEGER,
	right_edge_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(output) REFERENCES "Sequence" (id),
	FOREIGN KEY(left_edge_id) REFERENCES "SequenceCut" (id),
	FOREIGN KEY(right_edge_id) REFERENCES "SequenceCut" (id)
);
CREATE TABLE "RestrictionEnzymeDigestionSource" (
	output INTEGER,
	type TEXT,
	id INTEGER NOT NULL,
	left_edge_id INTEGER,
	right_edge_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(output) REFERENCES "Sequence" (id),
	FOREIGN KEY(left_edge_id) REFERENCES "RestrictionSequenceCut" (id),
	FOREIGN KEY(right_edge_id) REFERENCES "RestrictionSequenceCut" (id)
);
CREATE TABLE "AssemblyJoinComponent" (
	id INTEGER NOT NULL,
	sequence INTEGER NOT NULL,
	reverse_complemented BOOLEAN NOT NULL,
	location_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(sequence) REFERENCES "Sequence" (id),
	FOREIGN KEY(location_id) REFERENCES "SimpleSequenceLocation" (id)
);
CREATE TABLE "AssemblySource" (
	circular BOOLEAN,
	output INTEGER,
	type TEXT,
	id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(output) REFERENCES "Sequence" (id)
);
CREATE TABLE "PCRSource" (
	forward_primer INTEGER NOT NULL,
	reverse_primer INTEGER NOT NULL,
	circular BOOLEAN,
	output INTEGER,
	type TEXT,
	id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(forward_primer) REFERENCES "Primer" (id),
	FOREIGN KEY(reverse_primer) REFERENCES "Primer" (id),
	FOREIGN KEY(output) REFERENCES "Sequence" (id)
);
CREATE TABLE "LigationSource" (
	circular BOOLEAN,
	output INTEGER,
	type TEXT,
	id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(output) REFERENCES "Sequence" (id)
);
CREATE TABLE "HomologousRecombinationSource" (
	circular BOOLEAN,
	output INTEGER,
	type TEXT,
	id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(output) REFERENCES "Sequence" (id)
);
CREATE TABLE "GibsonAssemblySource" (
	circular BOOLEAN,
	output INTEGER,
	type TEXT,
	id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(output) REFERENCES "Sequence" (id)
);
CREATE TABLE "RestrictionAndLigationSource" (
	circular BOOLEAN,
	output INTEGER,
	type TEXT,
	id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(output) REFERENCES "Sequence" (id)
);
CREATE TABLE "CRISPRSource" (
	circular BOOLEAN,
	output INTEGER,
	type TEXT,
	id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(output) REFERENCES "Sequence" (id)
);
CREATE TABLE "OligoHybridizationSource" (
	overhang_crick_3prime INTEGER,
	forward_oligo INTEGER NOT NULL,
	reverse_oligo INTEGER NOT NULL,
	output INTEGER,
	type TEXT,
	id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(forward_oligo) REFERENCES "Primer" (id),
	FOREIGN KEY(reverse_oligo) REFERENCES "Primer" (id),
	FOREIGN KEY(output) REFERENCES "Sequence" (id)
);
CREATE TABLE "PolymeraseExtensionSource" (
	output INTEGER,
	type TEXT,
	id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(output) REFERENCES "Sequence" (id)
);
CREATE TABLE "AssemblyJoin" (
	id INTEGER NOT NULL,
	"AssemblySource_id" INTEGER,
	"PCRSource_id" INTEGER,
	"LigationSource_id" INTEGER,
	"HomologousRecombinationSource_id" INTEGER,
	"GibsonAssemblySource_id" INTEGER,
	"RestrictionAndLigationSource_id" INTEGER,
	"CRISPRSource_id" INTEGER,
	left_id INTEGER NOT NULL,
	right_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY("AssemblySource_id") REFERENCES "AssemblySource" (id),
	FOREIGN KEY("PCRSource_id") REFERENCES "PCRSource" (id),
	FOREIGN KEY("LigationSource_id") REFERENCES "LigationSource" (id),
	FOREIGN KEY("HomologousRecombinationSource_id") REFERENCES "HomologousRecombinationSource" (id),
	FOREIGN KEY("GibsonAssemblySource_id") REFERENCES "GibsonAssemblySource" (id),
	FOREIGN KEY("RestrictionAndLigationSource_id") REFERENCES "RestrictionAndLigationSource" (id),
	FOREIGN KEY("CRISPRSource_id") REFERENCES "CRISPRSource" (id),
	FOREIGN KEY(left_id) REFERENCES "AssemblyJoinComponent" (id),
	FOREIGN KEY(right_id) REFERENCES "AssemblyJoinComponent" (id)
);
CREATE TABLE "Source_input" (
	"Source_id" INTEGER,
	input_id INTEGER,
	PRIMARY KEY ("Source_id", input_id),
	FOREIGN KEY("Source_id") REFERENCES "Source" (id),
	FOREIGN KEY(input_id) REFERENCES "Sequence" (id)
);
CREATE TABLE "ManuallyTypedSource_input" (
	"ManuallyTypedSource_id" INTEGER,
	input_id INTEGER,
	PRIMARY KEY ("ManuallyTypedSource_id", input_id),
	FOREIGN KEY("ManuallyTypedSource_id") REFERENCES "ManuallyTypedSource" (id),
	FOREIGN KEY(input_id) REFERENCES "Sequence" (id)
);
CREATE TABLE "UploadedFileSource_input" (
	"UploadedFileSource_id" INTEGER,
	input_id INTEGER,
	PRIMARY KEY ("UploadedFileSource_id", input_id),
	FOREIGN KEY("UploadedFileSource_id") REFERENCES "UploadedFileSource" (id),
	FOREIGN KEY(input_id) REFERENCES "Sequence" (id)
);
CREATE TABLE "RepositoryIdSource_input" (
	"RepositoryIdSource_id" INTEGER,
	input_id INTEGER,
	PRIMARY KEY ("RepositoryIdSource_id", input_id),
	FOREIGN KEY("RepositoryIdSource_id") REFERENCES "RepositoryIdSource" (id),
	FOREIGN KEY(input_id) REFERENCES "Sequence" (id)
);
CREATE TABLE "AddGeneIdSource_input" (
	"AddGeneIdSource_id" INTEGER,
	input_id INTEGER,
	PRIMARY KEY ("AddGeneIdSource_id", input_id),
	FOREIGN KEY("AddGeneIdSource_id") REFERENCES "AddGeneIdSource" (id),
	FOREIGN KEY(input_id) REFERENCES "Sequence" (id)
);
CREATE TABLE "GenomeCoordinatesSource_input" (
	"GenomeCoordinatesSource_id" INTEGER,
	input_id INTEGER,
	PRIMARY KEY ("GenomeCoordinatesSource_id", input_id),
	FOREIGN KEY("GenomeCoordinatesSource_id") REFERENCES "GenomeCoordinatesSource" (id),
	FOREIGN KEY(input_id) REFERENCES "Sequence" (id)
);
CREATE TABLE "SequenceCutSource_input" (
	"SequenceCutSource_id" INTEGER,
	input_id INTEGER,
	PRIMARY KEY ("SequenceCutSource_id", input_id),
	FOREIGN KEY("SequenceCutSource_id") REFERENCES "SequenceCutSource" (id),
	FOREIGN KEY(input_id) REFERENCES "Sequence" (id)
);
CREATE TABLE "RestrictionEnzymeDigestionSource_input" (
	"RestrictionEnzymeDigestionSource_id" INTEGER,
	input_id INTEGER,
	PRIMARY KEY ("RestrictionEnzymeDigestionSource_id", input_id),
	FOREIGN KEY("RestrictionEnzymeDigestionSource_id") REFERENCES "RestrictionEnzymeDigestionSource" (id),
	FOREIGN KEY(input_id) REFERENCES "Sequence" (id)
);
CREATE TABLE "AssemblySource_input" (
	"AssemblySource_id" INTEGER,
	input_id INTEGER,
	PRIMARY KEY ("AssemblySource_id", input_id),
	FOREIGN KEY("AssemblySource_id") REFERENCES "AssemblySource" (id),
	FOREIGN KEY(input_id) REFERENCES "Sequence" (id)
);
CREATE TABLE "PCRSource_input" (
	"PCRSource_id" INTEGER,
	input_id INTEGER,
	PRIMARY KEY ("PCRSource_id", input_id),
	FOREIGN KEY("PCRSource_id") REFERENCES "PCRSource" (id),
	FOREIGN KEY(input_id) REFERENCES "Sequence" (id)
);
CREATE TABLE "LigationSource_input" (
	"LigationSource_id" INTEGER,
	input_id INTEGER,
	PRIMARY KEY ("LigationSource_id", input_id),
	FOREIGN KEY("LigationSource_id") REFERENCES "LigationSource" (id),
	FOREIGN KEY(input_id) REFERENCES "Sequence" (id)
);
CREATE TABLE "HomologousRecombinationSource_input" (
	"HomologousRecombinationSource_id" INTEGER,
	input_id INTEGER,
	PRIMARY KEY ("HomologousRecombinationSource_id", input_id),
	FOREIGN KEY("HomologousRecombinationSource_id") REFERENCES "HomologousRecombinationSource" (id),
	FOREIGN KEY(input_id) REFERENCES "Sequence" (id)
);
CREATE TABLE "GibsonAssemblySource_input" (
	"GibsonAssemblySource_id" INTEGER,
	input_id INTEGER,
	PRIMARY KEY ("GibsonAssemblySource_id", input_id),
	FOREIGN KEY("GibsonAssemblySource_id") REFERENCES "GibsonAssemblySource" (id),
	FOREIGN KEY(input_id) REFERENCES "Sequence" (id)
);
CREATE TABLE "RestrictionAndLigationSource_restriction_enzymes" (
	"RestrictionAndLigationSource_id" INTEGER,
	restriction_enzymes TEXT NOT NULL,
	PRIMARY KEY ("RestrictionAndLigationSource_id", restriction_enzymes),
	FOREIGN KEY("RestrictionAndLigationSource_id") REFERENCES "RestrictionAndLigationSource" (id)
);
CREATE TABLE "RestrictionAndLigationSource_input" (
	"RestrictionAndLigationSource_id" INTEGER,
	input_id INTEGER,
	PRIMARY KEY ("RestrictionAndLigationSource_id", input_id),
	FOREIGN KEY("RestrictionAndLigationSource_id") REFERENCES "RestrictionAndLigationSource" (id),
	FOREIGN KEY(input_id) REFERENCES "Sequence" (id)
);
CREATE TABLE "CRISPRSource_guides" (
	"CRISPRSource_id" INTEGER,
	guides_id INTEGER NOT NULL,
	PRIMARY KEY ("CRISPRSource_id", guides_id),
	FOREIGN KEY("CRISPRSource_id") REFERENCES "CRISPRSource" (id),
	FOREIGN KEY(guides_id) REFERENCES "Primer" (id)
);
CREATE TABLE "CRISPRSource_input" (
	"CRISPRSource_id" INTEGER,
	input_id INTEGER,
	PRIMARY KEY ("CRISPRSource_id", input_id),
	FOREIGN KEY("CRISPRSource_id") REFERENCES "CRISPRSource" (id),
	FOREIGN KEY(input_id) REFERENCES "Sequence" (id)
);
CREATE TABLE "OligoHybridizationSource_input" (
	"OligoHybridizationSource_id" INTEGER,
	input_id INTEGER,
	PRIMARY KEY ("OligoHybridizationSource_id", input_id),
	FOREIGN KEY("OligoHybridizationSource_id") REFERENCES "OligoHybridizationSource" (id),
	FOREIGN KEY(input_id) REFERENCES "Sequence" (id)
);
CREATE TABLE "PolymeraseExtensionSource_input" (
	"PolymeraseExtensionSource_id" INTEGER,
	input_id INTEGER,
	PRIMARY KEY ("PolymeraseExtensionSource_id", input_id),
	FOREIGN KEY("PolymeraseExtensionSource_id") REFERENCES "PolymeraseExtensionSource" (id),
	FOREIGN KEY(input_id) REFERENCES "Sequence" (id)
);
