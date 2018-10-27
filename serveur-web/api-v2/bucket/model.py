# Copyright (C) 2018 Roch D'Amour <roch.damour@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import json
from database.database import Database

class BucketModel(object):

	@staticmethod
	def find_by_id(id):
		"""
		Retreive a bucket's data and return it
		"""
		db = Database.get_instance()
		bucket_data = db.execute("SELECT * FROM BUCKET WHERE ID='"+str(id)+"'")
		if bucket_data:
			return bucket_data[0]
		else:
			return None

	@staticmethod
	def get_all():
		"""
		Retreive a bucket's data and return it
		"""
		db = Database.get_instance()
		bucket_data = db.execute("SELECT * FROM BUCKET")
		if bucket_data:
			return bucket_data
		else:
			return None

	@staticmethod
	def create(bucket):
		db = Database.get_instance()
		sql1 = "INSERT INTO bucket('name', 'id_plant', 'ip_address') VALUES"
		sql2 = "('" + str(bucket.name) + "', '" + str(bucket.id_plant) + "', '" + str(bucket.ip_address) + "');"

		db.execute(sql1+sql2)
		bucket_data = db.execute("SELECT * FROM BUCKET ORDER BY ID DESC LIMIT 1")
		if bucket_data:
			return bucket_data[0]
		else:
			return None


	@staticmethod
	def update(bucket):
		db = Database.get_instance()
		sql = (
			"UPDATE bucket " +
			"set name = '"+ str(bucket.name) + "', " +
			"id_plant = '"+ str(bucket.id_plant) + "', " +
			"ip_address = '"+ str(bucket.ip_address) + "' " +
			" WHERE id='" + str(bucket.id) + "' "
			)

		print(db.execute(sql))
		return bucket

	@staticmethod
	def delete(bucket):
		try:
			db = Database.get_instance()
			sql = (
				"delete from bucket " +
				" WHERE id='" + str(bucket.id) + "' "
				)

			print(db.execute(sql))
			return True
		except:
			return False