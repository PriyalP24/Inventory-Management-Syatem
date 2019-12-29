def insert(connection,name,extime,mnftime,image_path,quantity,category):
    with connection.cursor() as cursor:
        sql = "INSERT INTO `item` (`name`, `extime`,`maftime`,`image`,`quantity`,`category`) VALUES (%s, %s,%s,%s,%s,%s)"
        cursor.execute(sql, (name, extime, mnftime, image_path, quantity, category))
        connection.commit()

def update(connection,quantity,inventory_id):
    with connection.cursor() as cursor:
        sql = "UPDATE `item` SET quantity = "+ quantity + " WHERE `id`="+inventory_id;
        cursor.execute(sql,())
    connection.commit()
    connection.close()

def delete(connection,data):
    with connection.cursor() as cursor:
        for id in data:

            sql = "DELETE FROM item WHERE id=%s"


            cursor.execute(sql,(id))

            connection.commit()
        connection.close()

def SearchByName(connection,name):
    with connection.cursor() as cursor:
        sql = "SELECT * from item WHERE Name = %s"
        cursor.execute(sql,(name,))
        result = cursor.fetchall()

        connection.commit()
        connection.close()
        return result

def SearchByCategory(connection,category):
    with connection.cursor() as cursor:
        sql = "SELECT * from item WHERE Category = %s"
        cursor.execute(sql,(category,))
        result = cursor.fetchall()
        connection.commit()
        connection.close()
        return result




def select(connection):
    with connection.cursor() as cursor:
        sql="SELECT * from item"
        cursor.execute(sql, ())
        result = cursor.fetchall()
        connection.commit()
        return result






