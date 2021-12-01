

def sort_contributions_max_to_min(Contributions):
          size = len(Contributions)
          for step in range(0, size) :
                    max_position = step
                    for position  in  range(step+1, size) :
                              if Contributions[position][1] > Contributions[max_position][1] : 
                                        max_position = position
                    var_temp = Contributions[step]
                    Contributions[step] = Contributions[max_position]
                    Contributions[max_position] =  var_temp


def obligation_calculator(Contributions, Total):
          size = len(Contributions)
          obligation= Total/size
          return obligation

def remaining_obligations_calculator(Contributions, obligation):
          remaining_obligations = []
          size = len(Contributions)
          for index in range(size):
                    membre = Contributions[index][0]
                    remaining_obligation = obligation - Contributions[index][1]
                    remaining_obligations +=[(membre, remaining_obligation)]
          return remaining_obligations

def total_contribution(Contributions):
          total = 0
          size = len(Contributions)
          for index in range(size):
                    obligation = Contributions[index][1]
                    total += obligation
          return total

def generate_message(remaining_obligations):
          messages = []
          for index in range(len(remaining_obligations)):
                    membre = remaining_obligations[index]
                    message = membre[0] 
                    if membre[1] > 0 :
                              message += " give "
                    else :
                              message += " take "
                    message += str(round(abs(membre[1]), 2))
                    messages += [message]
          return messages

if __name__ == "__main__":
          test = True
          print("===============================================")
          print("=")
          print("=    Welcome to contributions equilibrator")
          print("=    By Samir EL KHYATI")
          print("=")
          print("===============================================")
          Contributions = []
          while test :
                    command = input("equilibrator>")
                    command_words = command.split(" ")
                    if command_words[0] == "quit" and len(command_words) == 1 :
                              test = False
                    elif command_words[0] == "addcontributor" :
                              if len(command_words)  == 3 :
                                        try :
                                                  contibution = float(command_words[2])
                                                  contributor = command_words[1]
                                                  Contributions +=[(contributor, contibution)]
                                        except:
                                                  print(">The given price must be a real number")
                              else:
                                        ">Wrong command : please, addcontibutor must be followed with the contributor and the price !"
                    elif command_words[0] == "showcontributors" :
                              for i in Contributions:
                                        print("> "+i[0] +" gives"+ str(i[1]))
                    elif command_words[0] == "total" :
                              print("> "+ str(total_contribution(Contributions)))
                    elif command_words[0] == "resolve" :
                              if len(Contributions) == 0 :
                                        print(">Please add some contributors")
                              else:
                                        total = total_contribution(Contributions)
                                        obligation= obligation_calculator(Contributions, total)
                                        print(">Total price: "+str(total))
                                        print(">Obligation: "+str(round(obligation, 2)))
                                        print(">")
                                        print(">")
                                        remaining_obligations = remaining_obligations_calculator(Contributions, obligation)
                                        messages = generate_message(remaining_obligations)
                                        for line in messages:
                                              print("> " + line)
                                        
                    else:
                              print(">Inknown command : " + command_words[0] + " doesn't match any defined command")
