"""
napari command line viewer.
"""
import argparse
import numpy as np
from skimage import io

import napari


def main():
    parser = argparse.ArgumentParser(usage=__doc__)
    parser.add_argument('images', nargs='+', help='Images to view.')
    parser.add_argument('--layers', action='store_true',
                        help='Treat multiple input images as layers.')
    parser.add_argument('-m', '--multichannel', help='Treat images as RGB.',
                        action='store_true')
    args = parser.parse_args()
    with napari.app():
        images = io.ImageCollection(args.images, conserve_memory=False)
        if args.layers:
            napari.view(*images, multichannel=args.multichannel,
                            hide_menubar=False)
        else:
            image = np.stack(images, axis=0)
            napari.view(image, multichannel=args.multichannel,
                        hide_menubar=False)
