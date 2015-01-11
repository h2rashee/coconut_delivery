import sys

jetStreams = []
mileCost = 0
endPoint = 0


def findShortestPath(curPos, curPath):
    if curPos < endPoint:
        regularFlight = getNextJetStream(curPos)

        fly = ((regularFlight[0]-curPos) * mileCost) + findShortestPath(regularFlight[0], curPath)

        if regularFlight:
            jet = min([st[2] + findShortestPath(st[1],
                curPath.append(st))
                for st in getCurrentJetStreams(curPos)], key = lambda x:x[1])
        else:
            return fly

        return fly if fly < jet else jet
    return 0


def getNextJetStream(curPos):
    '''Get the next jetstream that the swallow is sitting on'''
    for stream in jetStreams:
        if stream[0] > curPos:
            return stream
    return None


def getCurrentJetStreams(curPos):
    '''Given the current position, return the distance to the next jetstream'''
    lookingForSame = false
    streams = []

    for stream in jetStreams:
        if stream[0] >= curPos and not lookingForSame:
            lookingForSame = true
            streams.append(stream)
        elif lookingForSame and stream[0] == streams[0][0]:
            streams.append(stream)
        elif lookingForSame and stream[0] != streams[0][0]:
            return streams
    return streams


def findEndPoint():
    '''Find the end point that the swallow needs to travel'''
    '''based on the ending point of the farthest jetstream'''
    return max(jetStreams, key=lambda x:x[1])[1]


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
    endPoint = findEndPoint()
    print findShortestPath(pos, [])
