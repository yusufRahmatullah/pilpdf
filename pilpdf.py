from argparse import ArgumentParser
import os
from PIL import Image
import sys

ALLOWED_TYPES = ['bmp', 'jpg', 'jpeg', 'png']


class PilPdf:
    def __init__(self, input, output, resolution=100.0):
        self.input = input
        self.output = output
        self.resolution = resolution

        self._typ = 'dir' if os.path.isdir(self.input) else 'file'
        self._imgfs = []
        self._generate_imgfs()

    @property
    def is_dir(self) -> bool:
        return self._type == 'dir'

    @property
    def is_file(self) -> bool:
        return self._typ == 'file'

    def process(self):
        img = Image.open(self._imgfs[0]).convert('RGB')
        if self.is_file or len(self._imgfs) == 1:
            img.save(self.output, 'PDF', resolution=self.resolution)
        else:
            imgs = []
            for imgf in self._imgfs[1:]:
                imgs.append(Image.open(imgf).convert('RGB'))
            img.save(
                self.output, 'PDF',
                resolution=self.resolution, save_all=True, append_images=imgs
            )

    def validate(self):
        self._validate_input()
        self._validate_img_length()

    def _generate_imgfs(self):
        if self.is_file:
            ftype = self.input.rpartition('.')[-1]
            if ftype in ALLOWED_TYPES:
                self._imgfs.append(self.input)
            return
        ls = os.listdir(self.input)
        for fname in ls:
            ftype = fname.rpartition('.')[-1]
            if ftype in ALLOWED_TYPES:
                self._imgfs.append(os.path.join(self.input, fname))

    def _validate_input(self):
        if not os.path.exists(self.input):
            raise NameError(f'Input {self.input} is not exists')

    def _validate_img_length(self):
        if len(self._imgfs) == 0:
            raise ValueError(f'There is not image found on {self.input}')


def parse_args() -> PilPdf:
    parser = ArgumentParser('Convert Images to PDF using PIL')
    parser.add_argument(
        'input', help='Input File or Directory'
    )
    parser.add_argument(
        'output', help='Output filename'
    )
    parser.add_argument(
        '-r', '--resolution', default=100.0, type=float,
        help='PDF Resolution percentage'
    )
    args = parser.parse_args()
    return PilPdf(args.input, args.output, resolution=args.resolution)


def main():
    pilpdf = parse_args()
    pilpdf.validate()
    pilpdf.process()


if __name__ == '__main__':
    main()
