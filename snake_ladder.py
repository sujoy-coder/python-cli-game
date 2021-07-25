import random

class Player:
    def __init__(self, name):
        self.name = name
        self.pos = 0


class Game:
    def __init__(self):
        self.max_limit = 36
        self.snakes = {
            12:2,
            30:4,
            35:22
        }
        self.ladders = {
            3:16,
            15:25,
            21:32
        }

    def check_constraint(self, player, point):
        # update position based on snakes, ladder and 100 or 36 max limit...
        temp = player.pos+point
        if temp > self.max_limit:
            return
        if temp in self.ladders.keys():
            print(f'{player.name} got a Ladder \'H\'. [{temp} ---> {self.ladders[temp]}]')
            player.pos = self.ladders[temp]
            return
        if temp in self.snakes.keys():
            print(f'{player.name} got a Snake \'&\'. [{temp} ---> {self.snakes[temp]}]')
            player.pos = self.snakes[temp]
            return
        player.pos = temp
        return
        

    def player_position_update(self, player, point):
        if player.pos==0 and point!=1:
            return
        else:
            if point==1:
                self.check_constraint(player, point)
                if player.pos==self.max_limit:
                    return f'{player.name} Wins'
                return self.player_position_update(player, self.random_dice(player))
            else:
                self.check_constraint(player, point)
                if player.pos==self.max_limit:
                    return f'{player.name} Wins'
                return

    def random_dice(self, player):
        point = random.randint(1,6)
        print(player.name,' got : ',point)
        return point



def main():
    print('###########################################################')
    print('###  Welcome to Snake-Ladder Game, Play with the BOT   ####')
    print('###########################################################')
    # print('Image Showing...')
    game = Game()
    playerName = input('Enter your Name : ')
    player = Player(playerName)
    bot = Player('BOT')
    times = 0 
    yesorno = input('Do you want to start the Game (y/n) : ')
    if yesorno in ['y', 'Y', 'yes', 'Yes', 'YES']:
        while True:
            result = None
            if times%2==0:
                # player's turn in even time
                input(f'{player.name}\'s turn, Hit Enter : <-|')
                dice_point = game.random_dice(player)
                result = game.player_position_update(player, dice_point)
            else:
                # bot's turn in odd time
                dice_point = game.random_dice(bot)
                result = game.player_position_update(bot, dice_point)
            times += 1
            print(f'{player.name} position : {player.pos}\t\t{bot.name} position : {bot.pos}')
            # print('Image Showing...')
            if result:
                print(result)
                break
            print('<---------------------------------------------------->')
        print('###----Game Over----###')
        input('Enter any key to exit...')

    else:
        print('Exited. Thank You...')
        input('Enter any key to exit...')


  
main()
