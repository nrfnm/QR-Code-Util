"""
Quick script to generate QR Codes
"""
import argparse
from pathlib import Path
from datetime import datetime
import qrcode
from qrcode import ERROR_CORRECT_Q, ERROR_CORRECT_H, ERROR_CORRECT_L, ERROR_CORRECT_M

ERROR_MAP = {
    'L': ERROR_CORRECT_L,
    'M': ERROR_CORRECT_M,
    'Q': ERROR_CORRECT_Q,
    'H': ERROR_CORRECT_H
}

def generate_qr(data, output, box_size, border, fill, back, error_correction):
    """
    Method to generate QRCode using the qrcode library
    """
    qr = qrcode.QRCode(
        version=None,
        error_correction=ERROR_MAP[error_correction],
        box_size=box_size,
        border=border,
    )

    qr.add_data(data)
    qr.make(fit=True)

    out_dir = Path.home() / 'Documents' / 'qr_codes'
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / output

    img = qr.make_image(fill_color=fill, back_color=back)
    img.save(out_path)
    print(':white_check_mark: QR code generated successfully!')

def get_default_filename():
    """
    Returns the default filename for the QR code
    in the format: qr_<date_time>.png
    """
    return f"qr_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.png"

def main():
    """
    Adds cli arguments to the script and calls the generate_qr method
    """
    parser = argparse.ArgumentParser(description='Generate QR code.')

    parser.add_argument('data', help='Data to encode in the QR code.')

    parser.add_argument('-o', '--output',
                        default=get_default_filename(),
                        help='Output file name.')

    parser.add_argument('-s', '--size',
                        type=int,
                        default=100,
                        help='Size of the QR code box (in pixels).'
                        )
    parser.add_argument('-b', '--border',
                        type=int,
                        default=4,
                        help='Size of the border around the QR code (in pixels).'
                        )
    parser.add_argument('-f', '--fill',
                        default='black',
                        help='Color of the QR code box (in hex format).'
                        )
    parser.add_argument('--bg',
                        default='white',
                        help='Color of the background (in hex format).'
                        )
    parser.add_argument(
        '-e', '--error-correction',
        choices=['L', 'M', 'Q', 'H'],
        default='L',
        help='Error correction level: L=7%%, M=15%%, Q=25%%, H=30%%. Default: L'
    )


    args = parser.parse_args()

    generate_qr(args.data, args.output, args.size,
                args.border, args.fill, args.bg,
                args.error_correction)

    print('Done!')

if __name__ == '__main__':
    main()
