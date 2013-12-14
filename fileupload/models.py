from django.db import models


class Picture(models.Model):
    """
    This is a small demo using just two fields. ImageField depends on PIL or
    pillow (where Pillow is easily installable in a virtualenv. If you have
    problems installing pillow, use a more generic FileField instead.
    """

    picture_file = models.ImageField(upload_to="pictures")

    def __unicode__(self):
        return self.picture_file.name
