from django.db.models.fields.related_descriptors import (
    ForwardManyToOneDescriptor,
    ReverseOneToOneDescriptor,
    ReverseManyToOneDescriptor,
    ManyToManyDescriptor,
    ForwardOneToOneDescriptor,
)

DJANGO_RELATED_FIELD_DESCRIPTOR_CLASSES = (
    ForwardManyToOneDescriptor,
    ReverseOneToOneDescriptor,
    ReverseManyToOneDescriptor,
    ManyToManyDescriptor,
    ForwardOneToOneDescriptor,
)
