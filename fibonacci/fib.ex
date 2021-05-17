defmodule Fibonacci do

  def fib(n) do
    fib([0,1], n)
  end

  def fib(list, 2) do
    list
  end

  def fib(list, nth) do
    rev = Enum.reverse(list)
    fib( list ++ [hd(rev) + hd(tl(rev))] , nth - 1 )
  end

end

IO.inspect Fibonacci.fib(10)
