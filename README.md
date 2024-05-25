"""ETH Mugs Dataset."""

import os
from PIL import Image
import torch

from torch.utils.data import Dataset
from torchvision import transforms

from utils import IMAGE_SIZE, load_mask


# This is only an example - you DO NOT have to use it exactly in this form!
class ETHMugsDataset(Dataset):
    """Torch dataset template shared as an example."""

    def __init__(self, root_dir, mode="train"):
        """This dataset class loads the ETH Mugs dataset.

        It will return the resized image according to the scale and mask tensors
        in the original resolution.

        Args:
            root_dir (str): Path to the root directory of the dataset.
            mode (str): Mode of the dataset. It can be "train", "val" or "test"
        """
        self.mode = mode
        self.root_dir = root_dir

        # TODO: get image and mask paths
        self.rgb_dir = os.path.join(self.root_dir, "rgb")
        self.mask_dir = os.path.join(self.root_dir, "masks")
        self.image_paths = sorted(os.listdir(self.rgb_dir))

        # TODO: set image transforms - these transforms will be applied to pre-process the data before passing it through the model
        self.transform = None  # TO-DO

        print("[INFO] Dataset mode:", mode)
        print(
            "[INFO] Number of images in the ETHMugDataset: {}".format(len(self.image_paths))
        )

    def __len__(self):
        """Return the length of the dataset."""
        return len(self.image_paths)

    def __getitem__(self, idx):
        """Get an item from the dataset."""
        # Get the filename of the image corresponding to the given index
        image_name = self.image_paths[idx]
        # Construct the full path to the image file
        image_path = os.path.join(self.rgb_dir, image_name)
        # Construct the full path to the mask file by replacing the image file extension with "_mask.png"
        mask_path = os.path.join(self.mask_dir, image_name.replace("rgb.jpg", "mask.png"))

        # Load the image using PIL and convert it to RGB format
        image = Image.open(image_path).convert("RGB")

        # Load the mask using the custom function load_mask from utils.py
        mask = load_mask(mask_path)

        # Apply transformations if necessary
        if self.transform:
            image = self.transform(image)

        # Return the image and its corresponding mask
        return image, mask

