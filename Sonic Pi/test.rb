
define :bassdrum do |note1, duration, note2 = note1|
  use_synth :sine
  with_fx :hpf, cutoff: 100 do
    play note1 + 24, amp: 40, release: 0.01
  end
  with_fx :distortion, distort: 0.1, mix: 0.3 do
    with_fx :lpf, cutoff: 26 do
      with_fx :hpf, cutoff: 55 do
        bass = play note1, amp: 85, release: duration, note_slide: duration
        control bass, note: note2
      end
    end
  end
  sleep duration
end

live_loop :bass_test do
  bassdrum 36, 0.75
  if bools(0,0,1,0,0,0,1,0)[tick]
    bassdrum 36, 0.25, 40
    bassdrum 38, 0.5, 10
  else
    bassdrum 36, 0.75
  end
  bassdrum 36, 0.5, ring(10, 10, 10, 40)[look]
end

define :hh do |duration|
  use_synth :saw
  with_fx :hpf, cutoff: 100 do
    with_fx :distortion do
      play 100, attack: 0.01, release: 0.1
    end
    
  end
  sleep duration
end

live_loop :hh_test do
  hh 0.25
end



