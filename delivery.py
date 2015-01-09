import sys

jetStreams = []
mileCost = 0


def findShortestPath(curPos, curPath):
    pass


def getJetStreamCost(index):
    return jetStreams[index][2]


if __name__ == "__main__":
    try:
        with open('flight_paths.txt') as f:
            mileCost = int(f.readline())            # read first line
            for line in f:                          # read rest of lines
                jetStreams.append([int(x) for x in line.split()])
    except:
        print "Unexpected error while reading file"
        sys.exit(1)

    jetStreams = sorted(jetStreams, key=lambda x:x[0])

    pos = 0
    findShortestPath(pos, [])
