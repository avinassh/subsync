import argparse

def run():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument('media', metavar='MEDIA', type=str, nargs='+',
        help='media for which to synchronize subtitles')
    parser.add_argument('--graph', dest="graph", action='store_true',
        help='show graph for subtitle synchronization')
    parser.add_argument('-d', '--duration', dest='duration', type=int, metavar='SECONDS', default=60*15,
        help='duration (in seconds) of the sample audio length increases precision but reduces speed')
    parser.add_argument('-m', '--margin', dest='margin', type=int, metavar='SECONDS', default=12,
        help='the margin in which to search for a subtitle match')
    parser.add_argument('-s', '--start', dest='start', action='store_true',
        help='sample audio from the start of the media instad of the middle')

    args = parser.parse_args()


    from .media import Media
    media = [Media(m) for m in args.media]

    from .net import NeuralNet
    model = NeuralNet()

    for m in media:
        m.mfcc(duration=args.duration, seek=not args.start)
        for s in m.subtitles():
            s.sync(model, plot=args.graph, margin=args.margin)