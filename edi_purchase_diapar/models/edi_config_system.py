# Copyright (C) 2016-Today: Druidoo (<http://www.druidoo.io/>)
# @author: Druidoo
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html

from odoo import models, fields


class EdiConfigSystem(models.Model):
    _inherit = "edi.config.system"

    po_text_file_pattern = fields.Char(
        string="Purchase order File pattern",
        default="'LD%sH%s.C99' % self.env['edi.config.system'].\
        get_datenow_format_for_file()",
        required=True,
    )
    customer_code = fields.Char(default="33513", required=True)
    constant_file_start = fields.Char(default="HDIAPAR ", required=True)
    constant_file_end = fields.Char(default="*DIAPAR*DIAPAR", required=True)
    vrp_code = fields.Char(default="03", required=True)
    ftp_host = fields.Char(
        string="FTP Server Host", default="213.215.34.21", required=True
    )
    ftp_login = fields.Char(default="33513", required=True)
    ftp_password = fields.Char(default="divers", required=True)
    csv_relative_in_path = fields.Char(
        string="Relative path for IN interfaces",
        default="/Reception",
        required=True,
    )
    csv_relative_out_path = fields.Char(
        string="Relative path for OUT interfaces",
        default="/Envoi",
        required=True,
    )
