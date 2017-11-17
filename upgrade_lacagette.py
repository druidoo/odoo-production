# -*- coding: utf-8 -*-
from openerp.tools import config


def run(session, logger):
    """Update all modules."""
    if session.is_initialization:
        config['load_language'] = 'fr_FR'
        modules = [
            "cagette_custom_badge"
        ]
        session.install_modules(modules)
        logger.info(
            "Fresh database ! Installing foodcoops la louve- modules: %r",
            modules
        )
        session.env.cr.commit()
        return
    # specific case
    logger.info("Default upgrade procedure : updating all modules.")

    # expected installed module for a given version
    # format: { 'Num version': [ 'module to install', ...], }
    ins_modules_version = {}

    up_modules = ['all']
    ins_modules = []

    for version, module in ins_modules_version.items():
        if session.db_version <= version:
            ins_modules.extend(module)

    update_attachment(session, logger, ins_modules, up_modules)

    if ins_modules:
        session.update_modules_list()
        logger.info("installing modules %r", ins_modules)
        session.install_modules(ins_modules)

    if up_modules:
        logger.info("updating modules %r", up_modules)
        session.update_modules(up_modules)

    # I don't remember if this is necessary, anyway we commit!
    session.cr.commit()


def update_attachment(session, logger, ins_modules, up_modules):
    """Install large object in the db"""
    if session.db_version < '1.1' or not session.db_version:
        ins_modules.append('attachment_large_object')
        parameter = session.registry('ir.config_parameter')
        logger.info('Setup paramter to use advanced attachment')
        parameter.set_param(
            session.cr, session.uid, 'ir_attachment.location',
            'postgresql:lobject')
        session.cr.commit()
