""" LotR ALeP workflow (Part 2, after Strange Eons).
"""
import lotr


def main():  # pylint: disable=R0912
    """ Main function.
    """
    conf = lotr.read_conf()
    sets = lotr.get_sets(conf)

    for set_data in sets:
        set_id, set_name, _ = set_data
        for lang in conf['languages']:
            print('Processing set {} ({}):'.format(set_name, lang))
            skip_ids = lotr.get_skip_cards(set_id, lang)

            if 'db_octgn' in conf['outputs']:
                lotr.generate_jpg300_nobleed(set_id, lang, skip_ids)
            if 'pdf' in conf['outputs']:
                lotr.generate_png300_pdf(conf, set_id, lang, skip_ids)
            if 'makeplayingcards' in conf['outputs']:
                lotr.generate_png800_bleedmpc(conf, set_id, lang, skip_ids)
            if 'drivethrucards' in conf['outputs']:
                lotr.generate_jpg300_bleeddtc(conf, set_id, lang, skip_ids)

            if 'db' in conf['outputs']:
                lotr.generate_db(set_id, set_name, lang)
            if 'octgn' in conf['outputs']:
                lotr.generate_octgn(set_id, set_name, lang)
            if 'pdf' in conf['outputs']:
                lotr.generate_pdf(set_id, set_name, lang)
            if 'makeplayingcards' in conf['outputs']:
                lotr.generate_mpc(conf, set_id, set_name, lang)
            if 'drivethrucards' in conf['outputs']:
                lotr.generate_dtc(conf, set_id, set_name, lang)

    print('Done')


if __name__ == '__main__':
    main()
