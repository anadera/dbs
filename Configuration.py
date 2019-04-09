import warnings

from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session


class Configuration:

    def name_for_scalar_relationship(self, base, local_cls, referred_cls, constraint):
        name = referred_cls.__name__.lower()
        local_table = local_cls.__table__
        if name in local_table.columns:
            newname = name + self.naming_symbol
            warnings.warn("Already detected name %s present. using %s" % (name, newname))
            return newname
        return name

    def __init__(self, url, naming_symbol):
        self.naming_symbol = naming_symbol
        self.Base = automap_base()
        self.engine = create_engine(url)
        self.Base.prepare(self.engine, reflect=True, name_for_scalar_relationship=self.name_for_scalar_relationship)
        self.session = Session(self.engine)
