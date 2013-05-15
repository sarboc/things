#Hello world

#takes a variable (name) and says hello
def hello(name)
    puts "Hello, " + name + "!"
end

#sets variable name to "world" for first print
your_name = "world"
hello(your_name)

#gets user's name for second print
puts "I want to say hello to you, too.  What's your name?"
your_name = gets.chomp

#runs method again with user's name
hello(your_name)

#it would be rude not to say goodbye!
puts "Goodbye!"

#the end!


