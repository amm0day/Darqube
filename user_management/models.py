from bson import ObjectId
from django.db.models import Model, CharField, EmailField, Manager
from darqube.utils import get_collection_handle
from django.forms.models import model_to_dict


class UserModel(Model):
    objects = Manager()

    first_name = CharField(max_length=50)
    last_name = CharField(max_length=50)
    email = EmailField()

    class Meta:
        db_table = 'users'

    @classmethod
    def get_by_objectId(cls, oid: str):
        collection = get_collection_handle(cls._meta.db_table)
        document = collection.find_one({"_id": ObjectId(oid)})
        document["id"] = document.pop("_id")
        if document is None:
            raise cls.DoesNotExist(f"User with id={oid} not found")
        return cls(**document)

    def to_dict(self):
        d = model_to_dict(self)
        d["id"] = str(d["id"])
        return d

