--

sda = 2 -- SDA Pin
scl = 1 -- SCL Pin

s=0
m=0
h=0

function init_OLED(sda,scl) --Set up the u8glib lib
    sla = 0x3C
    i2c.setup(0, sda, scl, i2c.SLOW)
    disp = u8g.ssd1306_128x64_i2c(sla)
    disp:setFont(u8g.font_6x10)
    disp:setFontRefHeightExtendedText()
    disp:setDefaultForegroundColor()
    disp:setFontPosTop()
    --disp:setRot180()           -- Rotate Display if needed
end

function write_OLED() -- Write Display
    disp:firstPage()
    repeat
     disp:drawStr(50, 10, "Timer")
     disp:drawStr(40, 30,  string.format("%02d:%02d:%02d",h,m,s))
     disp:drawStr(20, 50, "ElectronicWings")
    until disp:nextPage() == false
end

-- Main Program
init_OLED(sda,scl)

tmr.alarm(0, 1000, 1, function() -- Every second increment clock and display
    s = s+1
    if s==60 then
     s=0
     m=m + 1
    end
    if m==60 then
     m=0
     h=h + 1
    end
    if h==13 then
     h=1
    end
    write_OLED()
end)
