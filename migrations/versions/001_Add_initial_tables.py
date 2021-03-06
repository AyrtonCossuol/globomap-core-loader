"""
   Copyright 2018 Globo.com

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""
from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import MetaData
from sqlalchemy import String
from sqlalchemy import Table
from sqlalchemy import Text

meta = MetaData()

job = Table('job', meta,
            Column('id', Integer, primary_key=True),
            Column('uuid', String(50), nullable=False),
            Column('driver', String(50), nullable=True),
            Column('updates_count', Integer, nullable=False),
            Column('success_count', Integer, nullable=False),
            Column('completed', Boolean, nullable=False),
            Column('date_created', DateTime, nullable=False),
            )

job_error = Table('job_error', meta,
                  Column('id', Integer, primary_key=True),
                  Column('uuid', String(50), nullable=False),
                  Column('request_body', Text, nullable=False),
                  Column('response', Text, nullable=False),
                  Column('status_code', String(3), nullable=True),
                  Column('job_id', Integer, ForeignKey(
                      'job.id', ondelete='CASCADE'), nullable=False)
                  )


def upgrade(migrate_engine):
    meta.bind = migrate_engine
    job.create()
    job_error.create()


def downgrade(migrate_engine):
    meta.bind = migrate_engine
    job_error.drop()
    job.drop()
