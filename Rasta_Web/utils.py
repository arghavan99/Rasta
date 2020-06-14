from django.core.exceptions import ValidationError


def validate_image_size(image):
    limit_mb = 5
    file_size = image.file.size
    if file_size > limit_mb * 1024 * 1024:
        raise ValidationError("Max size of file is %s MB" % limit_mb)


def validate_file_size(file):
    limit_mb = 10
    file_size = file.file.size
    if file_size > limit_mb * 1024 * 1024:
        raise ValidationError("Max size of file is %s MB" % limit_mb)
