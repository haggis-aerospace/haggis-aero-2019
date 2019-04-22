#include "mode.h"
#include "Plane.h"

bool ModeCircle::_enter()
{
    // the altitude to circle at is taken from the current altitude
    plane.throttle_allows_nudging = false;
    plane.auto_throttle_mode = true;
    plane.auto_navigation_mode = true;
    plane.next_WP_loc.alt = plane.current_loc.alt;

    return true;
}


// FTS andgles declared
void Plane::set_fts_angles()
{
  nav_pitch_cd = g.fts_pitch;
  nav_roll_cd = g.fts_roll;
  SRV_Channels::set_output_limit(SRV_Channel::k_throttle, SRV_Channel::SRV_CHANNEL_LIMIT_MIN);
  SRV_Channels::set_output_limit(SRV_Channel::k_throttleLeft, SRV_Channel::SRV_CHANNEL_LIMIT_MIN);
  SRV_Channels::set_output_limit(SRV_Channel::k_throttleRight, SRV_Channel::SRV_CHANNEL_LIMIT_MIN);
}

void ModeCircle::update()
{
    /* we have no GPS installed and have lost radio contact
    // or we just want to fly around in a gentle circle w/o GPS,
    // holding altitude at the altitude we set when we
    // switched into the mode
    plane.nav_roll_cd  = plane.roll_limit_cd / 3;
    plane.update_load_factor();
    plane.calc_nav_pitch();

*/

    plane.set_fts_angles();
}
