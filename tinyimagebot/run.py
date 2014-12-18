from multiprocessing import Process
import stream
import image_processor


if __name__ == "__main__":

    stream = Process(target=stream.run)
    image_processor = Process(target=image_processor.run)

    stream.start()
    image_processor.start()

    stream.join()
    image_processor.join()