import time

class TetrisGame(object):
    def run(self):
        running = True
        lastTime = time.time_ns()
        unprocessed = 0
        nsPerTick = 1000000000.0 / 60
        ticks = 0
        frames = 0
        lastTimer1 = int(time.time()*1000.0)
        
        while (running):
            now = time.time_ns()
            unprocessed += (now - lastTime) / nsPerTick
            lastTime = time.time_ns()
            shouldRender = True
            while (unprocessed >= 1):
                ticks += 1
                # app.tick()
                unprocessed -= 1
                shouldRender = True
            
            time.sleep(0.002) # sleep for 2 milliseconds
            
            if (shouldRender):
                frames += 1
                # app.render()
            
            if (int(time.time()*1000.0) - lastTimer1) > 1000:
                lastTimer1 += 1000
                print("ticks: " + str(ticks)  + ", fps: " + str(frames))
                frames = 0
                ticks = 0
        
    def tick(self):
        print("update game state here!")
    
    def render(self):
        print("render objects to screen here!")
        
if __name__ == '__main__':
    app = TetrisGame()
    app.run()