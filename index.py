import yaml

INDEX_FILE = 'stein-index.yml'

yaml.warnings({'YAMLLoadWarning': False})

def add_to_index(lemma, work, page_ref, ref_type=None):
    with open(INDEX_FILE) as f:
        index = yaml.load(f)

    reference = {'pageref': page_ref}

    # Makes sure ref_type 'p' is a child of 'lemma' instead of 'work'
    if ref_type != 'p' and ref_type != None:
         reference['reftype'] = ref_type

    try:
        lemma_entry = index[lemma]
    except KeyError:
        # Makes sure ref_type 'p' is a child of 'lemma' instead of 'work'
        if ref_type == 'p':
            lemma_entry = {work: [reference]}
            lemma_entry['reftype'] = ref_type
        else:
            lemma_entry = {work: [reference]}
    else:
        try:
            lemma_entry[work].append(reference)
        except KeyError:
            lemma_entry[work] = [reference]

    index[lemma] = lemma_entry

    with open(INDEX_FILE, 'w') as f:
        yaml.dump(index, f)
