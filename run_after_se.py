""" LotR ALeP workflow (Part 2, after Strange Eons).
"""
import lotr


def main():
    """ Main function.
    """
    conf = lotr.read_conf()
    sets = lotr.get_sets(conf)

    for set_data in sets:
        set_id, set_name, _ = set_data
        print('Processing set ID {}:'.format(set_id))
        skip_ids = lotr.get_skip_cards(set_id)

        if 'db_octgn' in conf['outputs']:
            lotr.generate_jpg300_nobleed(set_id, skip_ids)
        if 'pdf' in conf['outputs']:
            lotr.generate_png300_pdf(conf, set_id, skip_ids)
        if 'makeplayingcards' in conf['outputs']:
            lotr.generate_png800_bleedmpc(conf, set_id, skip_ids)

        if 'db' in conf['outputs']:
            lotr.generate_db(set_id, set_name)
        if 'octgn' in conf['outputs']:
            lotr.generate_octgn(set_id)
        if 'pdf' in conf['outputs']:
            lotr.generate_pdf(set_id, set_name)
        if 'makeplayingcards_zip' in conf['outputs']:
            lotr.generate_mpc_zip(set_id, set_name)
        if 'makeplayingcards_7z' in conf['outputs']:
            lotr.generate_mpc_7z(set_id, set_name)

    print('Done')


if __name__ == '__main__':
    main()