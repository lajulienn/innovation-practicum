import pika
import mongoengine

class TextLine(mongoengine.Document):
    text = StringField(required=True)

def main():
    rabbit_connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq')
    channel = rabbit_connection.channel()
    
    mongoengine.connect('1-task-docker', host='db')

    channel.queue_declare('')
    for _, _, body in mq_channel.consume(''):
        TextLine(text=body).save()

if __name__ == "__main__":
    main()
