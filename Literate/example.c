<<<START>>>
<@ Includes @>
<@ Main @>


<<< Main >>>
void main() {
   <@ Greet @>
   <@ Calculate Euler's Constant @>
   <@ Report Euler's Constant @>
}

<<<Greet>>>
print_for_me("Hello World!")
print_for_me("It's quite a wonderful world, isn't it?!")
print_for_me("Which reminds me of the song...")
print_for_me("What a wonnnderfulll worlllld!")
print_for_me("The colooors of the rainbowww, ... so pretty in the sky ...!")

<<<Calculate Euler's Constant>>>
double e = 0.0;
long long factorial = 1;
for(int i=0; i<100; ++i) {
   factorial *= i+1;
   e += 1.0/factorial;
}

<<<Report Euler's Constant>>>
print_for_me("Euler's constant is:")
print_for_me(e);
