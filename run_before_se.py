""" LotR ALeP workflow (Part 1, before Strange Eons).
"""
import logging
import time
import lotr

logging.basicConfig(level=logging.INFO, format='%(asctime)s: %(message)s')


def main():
    """ Main function.
    """
    timestamp = time.time()
    conf = lotr.read_conf()
    lotr.clear_project_folders()
    lotr.download_sheet(conf)
    sets = lotr.get_sets(conf)

    changes = False
    for set_data in sets:
        set_id, set_name, set_row = set_data
        if 'octgn' in conf['outputs']:
            lotr.generate_octgn_xml(conf, set_name, set_row)

        for lang in conf['languages']:
            lotr.backup_previous_xml(conf, set_id, set_name, lang)
            lotr.generate_xml(conf, set_id, set_name, set_row, lang)
            lotr.update_xml(conf, set_id, set_name, lang)
            new_hash, old_hash = lotr.calculate_hashes(set_id, set_name, lang)
            if new_hash != old_hash:
                changes = True

            lotr.copy_raw_images(conf, set_id, set_name, lang)
            lotr.copy_xml(set_id, set_name, lang)

    if changes:
        lotr.create_project()
    else:
        logging.info('No changes since the last run, skipping creating the'
                     ' project')

    logging.info('Done (%ss)', round(time.time() - timestamp, 3))


if __name__ == '__main__':
    main()