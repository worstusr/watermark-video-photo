# Watermark Tools for Photos and Videos

A collection of simple yet powerful Python scripts to apply professional watermarks to photos and videos. Perfect for photographers, videographers, and content creators who want to protect their work while maintaining visual quality.

## Features

### Photo Watermarking (`photo-wm.py`)
- ✅ Adds customizable text watermarks to all images in a folder
- ✅ Semi-transparent watermark with optimized settings
- ✅ Automatic font size calculation based on image dimensions
- ✅ Option to backup original files
- ✅ Maintains high image quality (95% quality preservation)
- ✅ Works with JPG, JPEG, and PNG formats

### Video Watermarking (`video-wm.py`)
- ✅ Embeds watermark text on videos using FFmpeg
- ✅ Preserves original audio quality
- ✅ Compatible with MP4, MOV, and AVI formats
- ✅ Creates preview files without modifying originals
- ✅ Simple batch processing

## Requirements

### For Photo Watermarking
- Python 3.6+
- Pillow library (`pip install Pillow`)

### For Video Watermarking
- Python 3.6+
- FFmpeg installed and accessible in PATH

## Usage

### Photo Watermarking

1. Create a folder named `jpeg` in the same directory as the script
2. Place your photos inside the `jpeg` folder
3. Run the script:
   ```
   python photo-wm.py
   ```
4. Follow the prompts to choose backup options

### Video Watermarking

1. Create a folder named `originals` in the same directory as the script
2. Place your videos inside the `originals` folder
3. Run the script:
   ```
   python video-wm.py
   ```
4. Watermarked preview videos will be saved in the `preview` folder

## Customization

Both scripts can be easily customized:

### Photo Watermark
- Edit `WATERMARK_TEXT` to change the watermark message
- Adjust `OPACITY` value (0.0-1.0) to make the watermark more or less visible
- Change `COLOR` tuple (RGB) to modify watermark color
- Modify `MARGIN` to reposition the watermark

### Video Watermark
- Edit the FFmpeg drawtext parameters in the `cmd` list to customize text, position, size, or opacity

## License

MIT License - Feel free to use and modify for your projects!

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests with improvements.
