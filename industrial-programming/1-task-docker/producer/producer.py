import sys
import pika

def main():
    rabbit_connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
    channel = rabbit_connection.channel()
    
    for line in sys.stdin:
        channel.basic_publish('', '', line.rstrip('\n'))

    channel.close()
    rabbit_connection.close()

if __name__ == "__main__":
    main()
