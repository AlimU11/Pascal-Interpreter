program Main;

procedure Alpha(a : integer; b : integer); { 8, 7 }
var x : integer;

   procedure Beta(a : integer; c : integer); { 5, 10 }
   var x : integer;
   begin
      x := a * 10 + b * 2 + c; { 74 }
   end;

begin
   x := (a + b ) * 2; { 30 }

   Beta(5, 10);      { procedure call }
end;

begin { Main }

   Alpha(3 + 5, 7);  { procedure call }

end.  { Main }
